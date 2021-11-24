# -*- codeing = utf-8 -*-
# @Time : 2021/11/14 19:01
# @Author : DongYun
# @File : 883.三维形体投影面积.py
# @Software : PyCharm
from typing import List
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        temp = grid[0]
        #计算俯视图面积
        for g in grid:
            area +=(len(g) - g.count(0)+max(g))
        # 计算y-z面积
            for index in range(len(temp)):
                temp[index] = max(temp[index],g[index])
        return area+sum(temp)



print(Solution().projectionArea([[1,0],[0,2]]))