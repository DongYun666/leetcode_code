# -*- codeing = utf-8 -*-
# @Time : 2021/10/12 9:08
# @Author : DongYun
# @File : 58.最后一个单词的长度.py
# @Software : PyCharm
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
