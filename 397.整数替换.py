# -*- codeing = utf-8 -*-
# @Time : 2021/11/20 20:38
# @Author : DongYun
# @File : 397.整数替换.py
# @Software : PyCharm
# 给定一个正整数n ，你可以做如下操作：
#
# 如果n是偶数，则用n / 2替换n 。
# 如果n是奇数，则可以用n + 1或n - 1替换n 。
# n变为 1 所需的最小替换次数是多少？
class Solution:
    def integerReplacement(self, n: int) -> int:
        def dfs(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return dfs(n/2)+1
            else:
                return min(dfs(n+1),dfs(n-1)) +1

        return dfs(n)
    def integerReplacement2(self, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        print(dp)
        def dfs(n,dp):
            if n == 1:
                return 0
            if n % 2 == 0:
                return dfs(n/2,dp)+1
            else:
                return min(dfs(n+1,dp),dfs(n-1,dp)) +1

        return dfs(n,dp)
print(Solution().integerReplacement2(7))