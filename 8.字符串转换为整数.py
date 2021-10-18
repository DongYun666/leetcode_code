# -*- codeing = utf-8 -*-
# @Time : 2021/9/28 21:10
# @Author : DongYun
# @File : 8.字符串转换为整数.py
# @Software : PyCharm
class Solution:
    def myAtoi(self,s:str):
        s = bytearray(s.strip(),encoding='utf-8')
        for i in range(len(s)-1):
            if s[i] != '-' or s[i] not in range(49,58):
                s[i] = 4
        return str(s).strip('*')
print(Solution().myAtoi("    -19    "))