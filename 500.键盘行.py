# -*- codeing = utf-8 -*-
# @Time : 2021/10/31 20:14
# @Author : DongYun
# @File : 500.键盘行.py
# @Software : PyCharm
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word_dict = {
            1:"qwertyuiop",
            2:"asdfghjkl",
            3:"zxcvbnm"
        }
        resoult = []
        for w in word_dict.keys():
            print(w)
        for word in words:
            flag = True
            index = 0
            for w in word_dict.keys():
                if word[0].lower() in word_dict.get(w):
                    index = w
            for ch in word[1:]:
                if ch.lower() not in word_dict.get(index):
                    flag = False
            if flag:
                resoult.append(word)
        return resoult

print(Solution().findWords(["adsdf","sfd"]))
# print(ord('a'))