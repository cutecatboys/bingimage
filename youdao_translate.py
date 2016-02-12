#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import urllib2

class ServiceError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        self._preprocess()

        return repr(self.reason)

    def _preprocess(self):
        err_code = {
                0: "Normal",
                20: "The text is too long",
                30: "Cannot process",
                40: "Unsupported language",
                50: "Invalid key",
                60: "No result"
                }

        self.reason = err_code[self.value]

class YoudaoTranslate:

    def __init__(self, key):
        self._key = key
        self._url = 'http://fanyi.youdao.com/openapi.do?keyfrom=cxvsdffd33&key='+self._key+'&type=data&doctype=json&version=1.1&q='

    def update_key(self, key):
        self._key = key
        self._url = 'http://fanyi.youdao.com/openapi.do?keyfrom=cxvsdffd33&key='+self._key+'&type=data&doctype=json&version=1.1&q='

    def _get_content(self, word):
        content = urllib2.urlopen(self._url + word)
        self._result = json.load(content)

    def _print_stars(self):
        print '****************'

    def print_result(self, word):
        self._get_content(word)
        if self._result['errorCode'] != 0:
            _print_stars()
            print 'Basic explains'
            for explain in self._result['basic']['explains']:
                print explain

            _print_stars()
