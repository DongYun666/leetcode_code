# -*- codeing = utf-8 -*-
# @Time : 2021/11/17 21:27
# @Author : DongYun
# @File : 318.最大单词长度成积.py
# @Software : PyCharm
from collections import defaultdict
from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d, ans = defaultdict(int), 0
        print(d)
        for w in words:
            s = set(w)
            print(s)
            # 用排序后拼接的字符串作为哈希值
            he = "".join(sorted(s))
            print(he)
            print(d[he])
            if d[he] < len(w):
                for other in d:
                    # 取出来的字符串再取集合，集合没有交集才有可能作为答案
                    if not set(other) & s:
                        ans = max(ans, len(w) * d[other])
                d[he] = len(w)
        return ans

print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))