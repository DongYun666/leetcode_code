# -*- codeing = utf-8 -*-
# @Time : 2021/11/13 15:36
# @Author : DongYun
# @File : 520.检测大写字母.py
# @Software : PyCharm
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return len(word) == 1 or word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())


print(Solution().detectCapitalUse("Leetcode"))


