# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 16:20
# @Author : DongYun
# @File : 421.Fizz Buzz.py
# @Software : PyCharm
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resoult = []
        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 != 0:
                resoult.append("Fizz")
            elif num % 5 == 0 and num % 3 != 0:
                resoult.append("Buzz")
            elif num % 3 == 0 and num % 5 ==0:
                resoult.append("FizzBuzz")
            else:
                resoult.append(str(num))
        return resoult

print(Solution().fizzBuzz(15))

