# -*- codeing = utf-8 -*-
# @Time : 2021/11/1 15:19
# @Author : DongYun
# @File : 575.分糖果.py
# @Software : PyCharm
from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        return 0

# print(Solution().distributeCandies([1,1,2,2,3,3]))

def getNext(m):
    if len(m) == 1:
        return [-1]
    next = [-1,0]
    i = 2
    cn = 0
    while i < len(m):
        if m[i-1] == m[cn]:
            cn+=1
            next.append(cn)
            i+=1
        elif cn > 0:
            cn = next[cn]
        else:
            i+=1
            next.append(0)
def getIndexOf(s,m):
    if s or m or len(m) < 1 or len(s) <len(m):
        return -1
    i1,i2 = 0,0
    next = getNext(m)
    while i1 < len(s) and i2 < len(m):
        if s[i1] == m[i2]:
            i1+=1
            i2+=1
        elif next[i2] == -1:
            i1+=1
        else:
            i2 = next[i2]
    return i1 - i2 if i2 == len(m) else -1

# print(getIndexOf("abcaabcabcd","abcd"))











