# -*- codeing = utf-8 -*-
# @Time : 2021/9/29 18:38
# @Author : DongYun
# @File : test.py
# @Software : PyCharm
class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        tot = sum(machines)
        n = len(machines)
        if tot % n:
            return -1
        avg = tot // n
        ans,s = 0,0
        for num in machines:
            num -= avg
            s+=num
            ans = max(ans,abs(s),num)
        return ans
print(Solution().findMinMoves([4,0,0,4]))