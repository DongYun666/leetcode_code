# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 15:27
# @Author : DongYun
# @File : 972.相等的有理数.py
# @Software : PyCharm
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        flag = False
        s_list = s.split(".")
        t_list = t.split(".")
        if s_list[0] == t_list[0]:
            flag = True
        s1_list = s_list[1].replace("(","").replace(")","")
        t1_list = t_list[1].replace("(","").replace(")","")
        print(s1_list,t1_list)
        if s1_list == t1_list or s1_list.find(t1_list) or t1_list.find(s1_list):
            flag = True
        else:
            flag = False
        return flag

print(Solution().isRationalEqual("0.(52)5","0.5(25)"))
# print(Solution().isRationalEqual( "0.1666(6)", "0.166(66)"))