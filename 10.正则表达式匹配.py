# -*- codeing = utf-8 -*-
# @Time : 2021/11/21 16:02
# @Author : DongYun
# @File : 10.正则表达式匹配.py
# @Software : PyCharm
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(s,p,s_index,p_index):
            if s_index == len(s):
                return True
            elif s_index == len(s) or p_index == len(p):
                return False
            if s[s_index] == p[p_index]:
                return dfs(s,p,s_index+1,p_index+1)
            elif p_index == len(p):
                return False
            elif p[p_index] == ".":
                return dfs(s,p,s_index+1,p_index+1)
            elif p[p_index] == "*":
                return dfs(s,p,s_index+1,p_index-1)
            elif s_index != p_index and p[p_index+1] == "*":
                return dfs(s,p,s_index,p_index+2)
            else:
                return False
        return dfs(s,p,0,0)
print(Solution().isMatch("mississippi","mis*is*ip*."))
