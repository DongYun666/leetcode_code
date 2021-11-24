# -*- codeing = utf-8 -*-
# @Time : 2021/10/30 17:12
# @Author : DongYun
# @File : 260.只出现一次的数字.py
# @Software : PyCharm
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        xor_x = 0
        for n in nums:
            diff ^= n
        eor = diff & (-diff)  #最diff最后一位1的位置
        for x in nums:
            if eor & x == eor:
                xor_x ^= x
        return [xor_x,xor_x^diff]

print(Solution().singleNumber([1,1,2,3,4,4,3,5,2]))

import functools
def singleNumber(nums: List[int]) -> List[int]:
    ret = functools.reduce(lambda x, y: x ^ y, nums)
    div = 1
    while div & ret == 0:
        div <<= 1
    a, b = 0, 0
    for n in nums:
        if n & div:
            a ^= n
        else:
            b ^= n
    return [a, b]
print(singleNumber([1,1,2,3,4,4,3,5,2,6]))


def f(a,b):
    c= ((a-b)>>31)&1
    return a*(c^1)+b*c
print(f(-4,-8))




