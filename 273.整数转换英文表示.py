# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 12:29
# @Author : DongYun
# @File : 273.整数转换英文表示.py
# @Software : PyCharm
singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0 :
            return ""
        resoult = ""
        while num != 0:
            if num % 100 != 0:
                resoult+=singles[num//100]+" "+"Hundred"+" "
                num -= (num //100)*100
            if num % 10 != 0:
                resoult += tens[num // 10] + " "
                num -= (num // 10)*10
            if num != 0:
                resoult += singles[num]
                num-=num
        return resoult
print(Solution().numberToWords(123))