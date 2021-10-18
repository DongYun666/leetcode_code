# -*- codeing = utf-8 -*-
# @Time : 2021/9/29 19:20
# @Author : DongYun
# @File : 9.回文数.py
# @Software : PyCharm
class Solution:
    def isPalindrome(self,x: int) -> bool:
        if x < 0 :
            return False
        s = list(str(x))
        return True if s == list(reversed(s)) else False
print(Solution().isPalindrome(10))
