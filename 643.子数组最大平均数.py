# -*- codeing = utf-8 -*-
# @Time : 2021/10/27 20:47
# @Author : DongYun
# @File : 643.子数组最大平均数.py
# @Software : PyCharm
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        for i in range(len(nums)-k+1):
            res = max(res,sum(nums[i:i+k])/k)
        return res
    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        k_sum = sum(nums[0:k])
        k_avg = k_sum/k
        for i in range(1,len(nums) - k + 1):
            k_sum -=nums[i-1]
            k_sum +=nums[i+k-1]
            k_avg = max(k_avg,k_sum/k)
        return k_avg


print(Solution().findMaxAverage2([1,12,-5,-6,50,3],4))
# print(-1/1)