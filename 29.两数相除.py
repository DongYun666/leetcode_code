# -*- codeing = utf-8 -*-
# @Time : 2021/10/12 9:41
# @Author : DongYun
# @File : 29.两数相除.py
# @Software : PyCharm
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res

print(Solution().divide(10,3))
