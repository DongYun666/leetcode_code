# -*- codeing = utf-8 -*-
# @Time : 2021/11/7 17:29
# @Author : DongYun
# @File : 537.复数乘法.py
# @Software : PyCharm
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1,num2 = num1.split("+"),num2.split("+")
        first = int(num1[0])*int(num2[0])
        second = int(num1[1].strip("i"))*int(num2[0])+int(num2[1].strip("i"))*int(num1[0])
        third = int(num1[1].strip("i"))*int(num2[1].strip("i"))*(-1)

        return str(first+third)+"+"+str(second)+"i"



print(Solution().complexNumberMultiply("1+-1i",  "1+-1i"))