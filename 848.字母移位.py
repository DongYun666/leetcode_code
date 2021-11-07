# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 15:02
# @Author : DongYun
# @File : 848.字母移位.py
# @Software : PyCharm
from itertools import accumulate
from typing import List

class Solution:
    #超时
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sum_list = [0]*len(shifts)
        for i in range(len(shifts)):
            new_shifts = shifts[i:len(shifts)]
            # print(new_shifts)
            sum_list[i] = sum(new_shifts)
        # print(sum_list)
        new_s = ''
        for index,ch in enumerate(s):
            # print(index,ch)
            new_s+=chr(ord('a')+(ord(ch)%26+sum_list[index]-ord('a'))%26)
            # print(new_s)

        return new_s

    def shiftingLetters2(self, S, shifts):
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(S):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)


    def shiftingLetters3(self, S: str, shifts: List[int]) -> str:
        # accumulate函数返回是一个可迭代对象，可以用在for里面，而不是最后的累加结果，如果我们想要的是直接的结果
        # accumulate函数用于计算前缀和
        cussum = list(accumulate(shifts[::-1]))[::-1]
        ret = ''
        for i in range(len(shifts)):
            ret += chr((ord(S[i]) + cussum[i] - 97) % 26 + 97)
        return ret

# print(Solution().shiftingLetters2('bad',[10,20,30]))
# print(type(sum([3,5,9])))
# print(ord('z'))

# my_pychar = "python"
# my_shechar = "shell"

