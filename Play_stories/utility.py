# -*- coding: utf-8 -*-

import os


class Text():
    # path 指定故事数据所在的路径
    def __init__(self, path):
        self.path = path
        self.story_file = []
        self.prepare_file()

    def prepare_file(self):
        for (root, dirs, files) in os.walk(self.path):
            for item in files:
                self.story_file.append(root+"/"+ item)
            break

    def isalnum(self, ch):
        if ch >= 'a' and ch <= 'z':
            return True
        if ch >= 'A' and ch <= 'Z':
            return True
        if ch >= '0' and ch <= '9':
            return True
        if ch == '.' or ch == '@' or ch == '_':
            return True
        return False

    def remove_error_symbol(self, text):
        res = ""
        for ch in text:
            if self.isalnum(ch):
                continue
            res = res + ch
        return res

