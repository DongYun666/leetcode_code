4# -*- codeing = utf-8 -*-
# @Time : 2021/10/31 20:45
# @Author : DongYun
# @File : 1.py
# @Software : PyCharm
class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a'*n if n%2==1 else 'a'*(n-1)+'b'

print(Solution().generateTheString(5))