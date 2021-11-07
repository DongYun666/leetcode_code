# -*- codeing = utf-8 -*-
# @Time : 2021/10/26 11:45
# @Author : DongYun
# @File : 1389.按既定顺序创建目标数组.py
# @Software : PyCharm
from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i,num in enumerate(nums):
            res.insert(index[i],num)
        return res


print(Solution().createTargetArray([1,2,3,4,0],[0,1,2,3,0]))