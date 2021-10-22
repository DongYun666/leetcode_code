# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 21:08
# @Author : DongYun
# @File : 3.无重复字符的最长字串.py
# @Software : PyCharm
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res