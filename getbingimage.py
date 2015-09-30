#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, Image, json, os

class BingError(Exception):
    def __init__(self):
        self.value = 'Network or URL occured an ERROR'

    def __str__(self):
        return repr(self.value)

class BingImage:
    def __init__(self, url = None):
        if url == None:
            self.bing_url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
        else:
            self.bing_url = url

    def preprocess(self):
        try:
            self.data = urllib2.urlopen(self.bing_url).read()
            self.json_data = json.loads(self.data)

            self.image_url = self.json_data['images'][0]['url']
            self.text = self.json_data['images'][0]['msg'][0]['text']
            self.title = self.json_data['images'][0]['msg'][0]['title']
            self.temp_path = '/tmp/Bing_' + self.title + '.jpg'
        except:
            raise BingError()

    def save(self, path = '/tmp/', file_path = None):
        if file_path == None:
            self.filename = path + 'Bing_' + self.title + '.jpg'
        else:
            self.filename = file_path

        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write(urllib2.urlopen(self.image_url).read())

    def show(self):
        if not os.path.exists(self.temp_path):
            self.save(file_path = self.temp_path)
        img = Image.open(self.temp_path)
        img.show()

if __name__ == '__main__':
    bing_instance = BingImage()
    bing_instance.preprocess()
    bing_instance.show()

    exit(0)
