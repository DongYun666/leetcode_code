# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 21:01
# @Author : DongYun
# @File : 1.两数之和.py
# @Software : PyCharm
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
