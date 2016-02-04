#!/usr/bin/env python
# -*-coding: utf-8 -*-

import urllib2
import os
from bs4 import BeautifulSoup
import progressbar
import imghdr

class down_pic:

    def __init__(self, url_list):
        self.url_list = url_list
        self.img_url = []
        self._num = 1

        for url in url_list:
            self.preprocess(url)

    def preprocess(self, url):
        html_content = urllib2.urlopen(url)
        soup = BeautifulSoup(html_content)

        imgs = soup.find_all('img')
        for img in imgs:
            if img.has_attr('class') and img['class'][0] == 'BDE_Image':
                self.img_url.append(img['src'])

    def downthem(self, auto_format = True):
        print 'A total of', len(self.img_url), 'pictures:'
        pbar = progressbar.ProgressBar()
        for url in pbar(self.img_url):
            with open(str(self._num) , 'w') as f:
                f.write(urllib2.urlopen(url).read())
            self._num = self._num + 1

        if auto_format:
            self.correct_type()

    def correct_type(self):
        files_list = [ img_file for img_file in os.listdir('.') if os.path.isfile(img_file) ]
        for file_name in files_list:
            img_type = imghdr.what(file_name)
            os.rename(file_name, file_name+'.'+img_type)


if __name__ == '__main__':
    url_list = []
    my_path = raw_input('Input the directory you want: ')
    if not os.path.exists(my_path):
        os.mkdir(my_path)
    os.chdir(my_path)

    num = int(raw_input('Input the number of URLs you want to download: '))
    for i in range(num):
        url_list.append(raw_input('Input the URL: '))

    img = down_pic(url_list)
    img.downthem()
