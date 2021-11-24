# -*- codeing = utf-8 -*-
# @Time : 2021/11/16 9:52
# @Author : DongYun
# @File : 391.完美矩形.py
# @Software : PyCharm
from typing import List
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x,y,a,b = rectangles[0][0],rectangles[0][1],rectangles[0][2],rectangles[0][3],
        area = 0
        for rectangle in rectangles:
            area += (rectangle[2]-rectangle[0])*(rectangle[3]-rectangle[1])
            x,y,a,b = min(x,rectangle[0]),min(y,rectangle[1]),max(a,rectangle[2]),max(b,rectangle[3])

        print(x,y,a,b)
        real_area = (a-x)*(b-y)
        return True if real_area == area else False

print(Solution().isRectangleCover([[0,0,1,1],[0,1,3,2],[1,0,2,2]]))