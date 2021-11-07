# -*- codeing = utf-8 -*-
# @Time : 2021/10/31 21:20
# @Author : DongYun
# @File : 剑指 Offer II 092. 翻转字符.py
# @Software : PyCharm
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        resoult = float('inf')
        s = list(s)
        for index,num in enumerate(s):
            if num == '1':
                resoult =  min(resoult,s[index:].count('0') if s[index:].count('1')>s[index:].count('0') else s[index:].count('1'))
        for index,num in enumerate(s[::-1]):
            if num == '1':
                resoult =  min(resoult,s[index:].count('0') if s[index:].count('1')>s[index:].count('0') else s[index:].count('1'))
        return resoult
print(Solution().minFlipsMonoIncr("010110"))