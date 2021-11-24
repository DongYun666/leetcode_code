# -*- codeing = utf-8 -*-
# @Time : 2021/11/20 20:33
# @Author : DongYun
# @File : 594.最长和谐子序列.py
# @Software : PyCharm
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res, begin = 0, 0
        for end in range(len(nums)):
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                res = max(res, end - begin + 1)
        return res

print(Solution().findLHS([1,3,2,2,5,2,3,7]))