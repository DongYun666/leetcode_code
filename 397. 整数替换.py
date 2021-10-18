# -*- codeing = utf-8 -*-
# @Time : 2021/10/16 21:04
# @Author : DongYun
# @File : 397. 整数替换.py
# @Software : PyCharm

class Solution:
    def integerReplacement(self, n: int) -> int:
        def track(n):
            if n == 1: return 0
            if n % 2 == 0:
                return 1 + track(n / 2)
            else:
                return 1 + min(track(n + 1), track(n - 1))
        return track(n)
    def integerReplacement2(self, n: int) -> int:
        count = 0
        while n != 1:
            if (n & 1) == 0:  # 偶数直接右移 1==>0001 偶数和1 & ==0
                n >>= 1
            else:
                n += -1 if (n & 2) == 0 or n == 3 else 1  # 奇数01或者3减一，其他加1
            count += 1
        return count
print(Solution().integerReplacement2(8))