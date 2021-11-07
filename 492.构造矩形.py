# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 11:05
# @Author : DongYun
# @File : 492.构造矩形.py
# @Software : PyCharm
from typing import List
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = [0,0]
        min_diff = area
        for x in range(1,int(math.sqrt(area))+1):
            if area % x == 0:
                bus = area //x
                if (bus - x) < min_diff:
                    min_diff = min((bus-x),min_diff)
                    res[0] = bus
                    res[1] = x
            else:
                continue
        return res
    def constructRectangle2(self, area: int) -> List[int]:
        new_area = math.sqrt(area)
        if str(new_area).split('.')[1]=='0':
            return [int(new_area),int(new_area)]
        else:
            start = int(new_area)
            while start != 0:
                if area % start ==0:
                    return [area//start,start]
                    break
                start-=1
    def constructRectangle3(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        while w >= 1:
            if area % w == 0:
                return [area // w, w]
            w -= 1

print(Solution().constructRectangle3(6))
# print(int(math.sqrt(5)))
print(type(type(4)))