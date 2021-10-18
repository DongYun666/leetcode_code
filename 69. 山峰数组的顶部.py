# -*- codeing = utf-8 -*-
# @Time : 2021/10/14 9:43
# @Author : DongYun
# @File : 69. 山峰数组的顶部.py
# @Software : PyCharm
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -1
        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break
        return ans
    def peakIndexInMountainArray2(self,arr: List[int]) -> int:
        return arr.index(max(arr))

print(Solution().peakIndexInMountainArray2([1,2,3,4,6,5,3,2,1]))