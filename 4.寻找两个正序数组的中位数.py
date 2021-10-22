# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 21:09
# @Author : DongYun
# @File : 4.寻找两个正序数组的中位数.py
# @Software : PyCharm
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1)+len(nums2)
        nums = nums1+nums2
        nums.sort()
        if length%2 == 0:
            return float(nums[int(length/2)]+nums[int(length/2-1)])/2
        else:
            return float(nums[int((length-1)/2)])