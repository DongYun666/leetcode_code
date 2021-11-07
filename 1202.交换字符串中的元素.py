# -*- codeing = utf-8 -*-
# @Time : 2021/10/31 21:03
# @Author : DongYun
# @File : 1202.交换字符串中的元素.py
# @Software : PyCharm
from typing import List
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        for change_pair in pairs:
            print(change_pair[0],change_pair[1])
            s[change_pair[0]],s[change_pair[1]] = s[change_pair[1]],s[change_pair[0]]
        return "".join(s)


print(Solution().smallestStringWithSwaps("dcab",[[0,3],[1,2]]))
