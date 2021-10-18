# -*- codeing = utf-8 -*-
# @Time : 2021/10/12 9:20
# @Author : DongYun
# @File : 66.加一.py
# @Software : PyCharm
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i]+=1
        while digits[i] == 10:
            digits[i]=0
            if i == 0:
                digits+=[0]
                digits[0]=1
            else:
                digits[i-1]+=1
            i-=1
        return digits
print(Solution().plusOne([1,2,9]))