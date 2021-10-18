# -*- codeing = utf-8 -*-
# @Time : 2021/10/17 22:39
# @Author : DongYun
# @File : 31.下一个排列.py
# @Software : PyCharm
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]):
        len_nums = len(nums)-1
        if len_nums !=0 :
            for n in range(len_nums,0,-1):
                if nums[n] > nums[n-1]:
                    break
            if n==1:
                if nums[n]< nums[0]:
                    nums.sort()
                else:
                    for i in range(len_nums, 0, -1):
                        if nums[i] > nums[0]:
                            break
                    temp = nums[i]
                    nums[i] = nums[0]
                    nums[0] = temp
                    # print(nums)
                    # print(nums[:1])
                    # print(nums[1:])
                    left_nums = nums[1:]
                    left_nums.sort()
                    nums = nums[:1]+left_nums
            else:
                temp = nums[n]
                nums[n] = nums[n-1]
                nums[n-1] = temp
        print(nums)

print(Solution().nextPermutation([1,3,2]))