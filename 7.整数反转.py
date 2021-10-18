# -*- codeing = utf-8 -*-
# @Time : 2021/9/28 20:45
# @Author : DongYun
# @File : 7.整数反转.py
# @Software : PyCharm
class Solution:
    def reverse(self,x: int)-> int:
        if x > 0:
            flag = True
        else:
            flag = False
        new_x = int(str(abs(x))[::-1])
        return  new_x if flag else -new_x
print(Solution().reverse(1534236469))