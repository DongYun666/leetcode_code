# -*- codeing = utf-8 -*-
# @Time : 2021/9/29 20:07
# @Author : DongYun
# @File : 12.整数转罗马数字.py
# @Software : PyCharm
class Solution:
    def intToRoman(self, num: int) -> str:
        s = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        resouolt = list()
        for value, sign in s.items():
            while num>= value:
                resouolt.append(sign)
                num -= value
            if num==0:
                break
        return "".join(resouolt)


print(Solution().intToRoman(20))
