# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 19:10
# @Author : DongYun
# @File : 229.求众数.py
# @Software : PyCharm
class Solution(object):
    def majorityElement(self, nums):
        count = {}
        resoult = []
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for x in count.keys():
            if count[x]> len(nums)//3:
                resoult.append(x)
        return  resoult
    def majorityElement2(self, nums):
        new_nums = list(set(nums))
        res = []
        for i in new_nums:
            if nums.count(i)>(len(nums)//3):
                res.append(i)
        return res

print(Solution().majorityElement2([-1,-1,-1]))