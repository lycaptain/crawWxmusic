# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib import request
import requests
import re
import shutil
import os
import json
import argparse
import traceback
import random
import math
import codecs


def get_all_link(file):
    with open(file, 'r+', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        for i in soup.find_all('a', target="_blank"):
            print(i.text.strip() + '\t' + i['href'], file=open('bomblab.txt', 'a+', encoding='utf-8'))
            # print(i['href'])
            # print(i.text.strip().strip('\n'))

def download(url):
    print('Downloading:',url)
    html = request.urlopen(url).read()
    return html

def crawl_mp3(name, last):
    with open('bomblab.txt', 'r', encoding='utf-8') as file:
        link_lists = file.readlines()
    url = "https://res.wx.qq.com/voice/getvoice?mediaid="
    path = "D:\jk\第四卷"
    url = url + last
    path = path + "\\" + name + ".mp3"
    r = requests.get(url)
    print('ok')
    print(path)
    with open(path, "wb") as f:
        f.write(r.content)
    f.close()

def start_download():
    with open('bomblab.txt', 'r', encoding='utf-8') as file:
        link_lists = file.readlines()
        for index, item in enumerate(link_lists):
            link = item.split('\t')[1]
            #link = "http://mp.weixin.qq.com/s?__biz=MzIyMjg4NDA1OA==&mid=2247485837&idx=1&sn=d74d7ba47f6ef477d2f11efbbcbc8895&chksm=e827f038df50792efcce67d3ef933cbc483874b36e71f0d843f2274c0fab3799d7c9272ad8bd&scene=21#wechat_redirect"
            html = download(link)
            soup = BeautifulSoup(html, 'lxml')
            #last = soup.find(id='voice_encode_fileid')
            a= soup.find('mpvoice')
            name = a['name']
            last = a['voice_encode_fileid']
            print(last)
            name = ''.join(name.split('|'))
            name = ''.join(name.split('间客'))
            name = ''.join(name.split())
            print(name)
            crawl_mp3(name,last)


if __name__ == '__main__':
    get_all_link("4.html")
    start_download()
