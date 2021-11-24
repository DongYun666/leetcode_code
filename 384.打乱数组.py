# -*- codeing = utf-8 -*-
# @Time : 2021/11/22 8:54
# @Author : DongYun
# @File : 384.全排列.py
# @Software : PyCharm
import random
from typing import List

class Solution:
    def __init__(self,nums: List[int]):
        self.nums = nums
        self.nums_backup = nums.copy()
    def reset(self) -> List[int] :
        return self.nums_backup
    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randint(1,len(self.nums)-1)
            self.nums[i],self.nums[j] = self.nums[j],self.nums[i]
        return self.nums
    # def shuffle(self) -> List[int] :
    #     def dfs(first = 0):
    #         if first == n:
    #             res.append(self.nums[:])
    #         for i in range(first,n):
    #             self.nums[first],self.nums[i] = self.nums[i],self.nums[first]
    #             dfs(first+1)
    #             self.nums[first],self.nums[i] = self.nums[i],self.nums[first]
    #     n = len(self.nums)
    #     res = []
    #     dfs()
    #     return res[random.randint(1,len(res)-1)]

if __name__ == '__main__':
    s = Solution([1,2,3])
    print(s.reset())
    n = 0
    while n != 100:
        print(s.shuffle())
        n+=1
    print("*"*40)
    print(s.reset())