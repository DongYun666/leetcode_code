# -*- codeing = utf-8 -*-
# @Time : 2021/11/11 17:43
# @Author : DongYun
# @File : 629. K个逆序对数组.py
# @Software : PyCharm
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        def dfs(n, k, ans=None):
            if n == k == 2 or n == k == 1 or (n==1 and k == 2) :
                return 0
            if (n == 2 and k == 1)or(n == 2 and k == 0)or (n == 1 and k == 0):
                return 1
            for i in range(k,-1,-1):
                ans += dfs(n-1,i,0)
            return ans%mod
        return dfs(n,k,0)%mod


# print(Solution().kInversePairs(4,2))

def kInversePairs(n: int, k: int) -> int:
    mod = 10 ** 9 + 7

    f = [1] + [0] * k
    for i in range(1, n + 1):
        g = [0] * (k + 1)
        for j in range(k + 1):
            g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
            g[j] %= mod
        f = g

    return f[k]
print(kInversePairs(7,11))





