# -*- codeing = utf-8 -*-
# @Time : 2021/10/18 9:10
# @Author : DongYun
# @File : 476.数字的补数.py
# @Software : PyCharm
class Solution:
    def findComplement(self, num: int) -> int:
        new_num = ""
        for i in bin(num)[2:]:
            new_num += "1" if i =="0" else "0"
        return int(new_num,2)

    def findComplement2(self, num: int) -> int:
        s,count = 1,0
        while s<=num:
            s<<=1
            count+=1
        return 2**count-num-1
    def findComplement3(self, num: int) -> int:
        s,count = 1,0
        while s<=num:
            s<<=1
            count+=1
        return int("1"*count,2)^num
    def findComplement4(self, num: int) -> int:
        new_num = 0
        for index,i in enumerate(bin(num)[2:]):
            new_num += int(str(1 ^ int(i,2)))*(2**index)
        return new_num
print(Solution().findComplement4(2))