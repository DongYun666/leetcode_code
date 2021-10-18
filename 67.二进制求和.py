# -*- codeing = utf-8 -*-
# @Time : 2021/10/15 21:18
# @Author : DongYun
# @File : 67.二进制求和.py
# @Software : PyCharm
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
print(Solution().addBinary("11","1"))
