# -*- codeing = utf-8 -*-
# @Time : 2021/10/9 19:26
# @Author : DongYun
# @File : 26.删除有序数组中的重复项.py
# @Software : PyCharm
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return len(nums)
        start , end  = 1,1
        while end!= len(nums):
            if nums[end] != nums[end-1]:
                nums[start] = nums[end]
                start+=1
                end+=1
            else:
                end+=1
        return  start


print(Solution().removeDuplicates([1]))
