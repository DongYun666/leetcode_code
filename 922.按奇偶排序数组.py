# -*- codeing = utf-8 -*-
# @Time : 2021/11/8 20:59
# @Author : DongYun
# @File : 922.按奇偶排序数组.py
# @Software : PyCharm
from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for index,num in enumerate(nums):
            if index%2!= num%2:
                for i,n in enumerate(nums[index+1:]):
                    if n % 2 == index%2:
                        nums[index],nums[index+i+1] = nums[index+i+1],nums[index]
                        break
        return nums

    def sortArrayByParityII2(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        i,j=0,1
        for x in nums:
            if x%2:
                ans[j]=x
                j+=2
            else:
                ans[i]=x
                i+=2
        return ans

print(Solution().sortArrayByParityII2([1,2]))