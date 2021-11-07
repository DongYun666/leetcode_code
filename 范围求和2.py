# -*- codeing = utf-8 -*-
# @Time : 2021/11/7 15:13
# @Author : DongYun
# @File : 范围求和2.py
# @Software : PyCharm
from typing import List
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return 0
        x_min = ops[0][0]
        y_min = ops[0][1]
        for op in ops:
            x_min = min(x_min,op[0])
            y_min = min(y_min,op[1])
        return x_min*y_min
print(Solution().maxCount(3,3,[]))