# -*- codeing = utf-8 -*-
# @Time : 2021/10/18 20:39
# @Author : DongYun
# @File : 面试题 16.10.生存人数.py
# @Software : PyCharm
from typing import List
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        len_data = len(birth)
        count = [0 for i in range(101)]
        def leijia(n,start):
            i=0
            while i!=n:
                count[start+i]+=1
                i+=1
        for i in range(len_data):
            n = death[i]-birth[i]+1
            leijia(n,birth[i]-1900)

        return count.index(max(count))+1900
    def maxAliveYear2(self, birth: List[int], death: List[int]) -> int:
        count = [0 for i in range(102)]
        age,sum = 0,0
        for i in range(len(birth)):
            count[birth[i]-1900]+=1
            count[death[i]-1899]-=1
        for n in range(len(count)):
            sum += count[n]
            if age<sum:
                age = sum
                year = n
        return 1900+year

    def maxAliveYear3(self, birth: List[int], death: List[int]) -> int:
        data = [0] * 103
        for i in range(len(birth)):
            data[birth[i] - 1900] += 1
            data[death[i] - 1899] -= 1
        max_, ans = data[0], 1900
        for i in range(1, len(data)):
            data[i] = data[i - 1] + data[i]
            if data[i] > max_:
                max_ = data[i]
                ans = i + 1900
        return ans
# print(Solution().maxAliveYear([1972,1908,1915,1957,1960,1948,1912,1903,1949,1977,1900,1957,1934,1929,1913,1902,1903,1901],[1997,1932,1963,1997,1983,2000,1926,1962,1955,1997,1998,1989,1992,1975,1940,1903,1983,1969]))
print(Solution().maxAliveYear3([1972,1908,1915,1957,1960,1948,1912,1903,1949,1977,1900,1957,1934,1929,1913,1902,1903,1901],[1997,1932,1963,1997,1983,2000,1926,1962,1955,1997,1998,1989,1992,1975,1940,1903,1983,1969]))