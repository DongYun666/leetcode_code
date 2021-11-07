# -*- codeing = utf-8 -*-
# @Time : 2021/10/27 21:09
# @Author : DongYun
# @File : 371.两整数之和.py
# @Software : PyCharm
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0 and b>0:
            b = ~b+1
        if b < 0 and a>0:
            b = ~b+1
        while b != 0 :
            a, b = a^b , (a & b)<<1
        return a
print(Solution().getSum(-20,30))