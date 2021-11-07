# -*- codeing = utf-8 -*-
# @Time : 2021/11/2 14:42
# @Author : DongYun
# @File : 32.最长有效括号.py
# @Software : PyCharm
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [""]*len(s)
        top = -1
        count=0
        for i in range(len(s)):
            if s[i] == "(":
                top += 1
                stack[top] = s[i]
            if s[i] == ")":
                if top != -1:
                    top -= 1
                    count+=1
                else:
                    count = 0

        return count*2


print(Solution().longestValidParentheses("()(()"))