# -*- codeing = utf-8 -*-
# @Time : 2021/10/20 13:54
# @Author : DongYun
# @File : 1232.缀点成线.py
# @Software : PyCharm
class Solution(object):
    def checkStraightLine(self, coordinates):
        return all((coordinates[1][0] - coordinates[0][0])*(y - coordinates[0][1]) ==
                 (coordinates[1][1] - coordinates[0][1])* (x - coordinates[0][0])
                 for x,y in coordinates[2:])
print(Solution().checkStraightLine([[0,0],[0,1],[0,-1]]))