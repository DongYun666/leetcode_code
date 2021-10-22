# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 21:11
# @Author : DongYun
# @File : 6.Z形变换.py
# @Software : PyCharm
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)