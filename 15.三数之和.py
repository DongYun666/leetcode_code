# -*- codeing = utf-8 -*-
# @Time : 2021/10/5 18:03
# @Author : DongYun
# @File : 15.三数之和.py
# @Software : PyCharm
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        resoult = []
        nums.sort()
        if len(nums) == 0:
            return resoult
        elif len(nums)==1 and nums[0] ==0:
            return resoult
        else:
            for index,value in enumerate(nums[0:-2]):
                start = index+1
                end = len(nums)-1
                while start != end:
                    if nums[start]+nums[end]+value == 0:
                        resoult.append([nums[start],nums[end],value])
                        start+=1
                        end-=1
                        break
                    if value+nums[start]<nums[end] :
                        end-=1
                    if value+nums[start]>nums[end] :
                        start+=1
        return resoult
print(Solution().threeSum([0,0,0]))
