# -*- codeing = utf-8 -*-
# @Time : 2021/10/26 11:13
# @Author : DongYun
# @File : 496.下一个更大的元素1.py
# @Software : PyCharm
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        flag = False
        res = []
        for i in nums1:
            for n2 in nums2[nums2.index(i):]:
                if n2>i:
                    res.append(n2)
                    flag=True
                    break
            if not flag:
                res.append(-1)
            flag = False
        return res

    def nextGreaterElement2(self, nums1, nums2):
        stack, hash = [], {}
        for n in nums2:
            while stack and stack[-1] < n:
                hash[stack.pop()] = n
            stack.append(n)
        res = [hash.get(x, -1) for x in nums1]
        return res
# print(Solution().nextGreaterElement2([2,4],[1,2,3,4]))
