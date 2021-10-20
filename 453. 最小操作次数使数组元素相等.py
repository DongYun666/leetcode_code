# -*- codeing = utf-8 -*-
# @Time : 2021/10/20 9:34
# @Author : DongYun
# @File : 453. 最小操作次数使数组元素相等.py
# @Software : PyCharm
class Solution(object):
    def minMoves(self, nums):
        return sum(nums)-min(nums)*len(nums)
print(Solution().minMoves([1,2,3,4]))