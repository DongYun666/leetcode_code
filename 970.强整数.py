# -*- codeing = utf-8 -*-
# @Time : 2021/10/12 10:46
# @Author : DongYun
# @File : 970.强整数.py
# @Software : PyCharm
from typing import List
import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ###报错[2,1,10]-->[9,2,3,5]
        # count_x,count_y =0,0
        # if x == 1:
        #     count_x = bound
        # elif y==1:
        #     count_y = bound
        # else:
        #     count_x = int(math.log((bound-1),x))+1
        #     count_y = int(math.log((bound-1),y))+1
        resoult = []
        for i in range(18):
            for j in range(18):
                if x**i+y**j <= bound:
                    resoult.append(x**i+y**j)
        return sorted(set(resoult))


print(Solution().powerfulIntegers(2,2,40000))