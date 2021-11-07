# -*- codeing = utf-8 -*-
# @Time : 2021/10/30 19:59
# @Author : DongYun
# @File : 1287. 有序数组中出现次数超过25%的元素.py
# @Software : PyCharm
import itertools
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)<4:
            return arr[0]
        count = len(arr) / 4
        k = 1
        pre = arr[0]
        for x in range(1,len(arr)):
            if arr[x] == pre:
                k +=1
            else:
                k =1
                pre = arr[x]
            if k > count:
                return arr[x]

print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))

