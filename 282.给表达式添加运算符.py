# -*- codeing = utf-8 -*-
# @Time : 2021/10/16 9:38
# @Author : DongYun
# @File : 282.给表达式添加运算符.py
# @Software : PyCharm
import re
from itertools import zip_longest, chain, product
from typing import List
o, ptn = ['', '+', '-', '*'], re.compile(r'[\D]0\d')
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr: List[str], i: int, res: int, mul: int):
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:  # 表达式开头不能添加符号
                    backtrack(expr, j + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+';
                    backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-';
                    backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*';
                    backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans

    def test(self, num: str, target: int):
        check = lambda expr: not ptn.search('+' + expr) and eval(expr) == target
        return [expr for expr in [''.join(chain(*zip_longest(num, ops, fillvalue=''))) for ops in product(o, repeat=len(num) - 1)] if check(expr)]

print(Solution().test("105",5))