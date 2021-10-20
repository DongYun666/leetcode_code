# -*- codeing = utf-8 -*-
# @Time : 2021/10/19 20:36
# @Author : DongYun
# @File : 703.数据流中的第K大元素.py
# @Software : PyCharm
import heapq
from typing import List
# 超时
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums
#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         print(sorted(self.nums)[len(self.nums)-self.k])
class KthLargest(object):

    def __init__(self, k, nums):

        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val):

        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]

## 或者通过快速排序+二分查找
if __name__ == '__main__':
    ans = KthLargest(3,[4,5,8,2])
    print(ans.add(3))
