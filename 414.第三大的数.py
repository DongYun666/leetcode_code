# -*- codeing = utf-8 -*-
# @Time : 2021/10/6 20:15
# @Author : DongYun
# @File : 414.第三大的数.py
# @Software : PyCharm
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        new_nums = sorted(set(nums),reverse=True)
        print(new_nums)
        if len(new_nums)<=2:
            return new_nums[1]
        else:
            return new_nums[2]

print(Solution().thirdMax([2,2,3,1]))