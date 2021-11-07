# -*- codeing = utf-8 -*-
# @Time : 2021/10/30 20:58
# @Author : DongYun
# @File : 394. 字符串解码.py
# @Software : PyCharm
class Solution:
    def decodeString(self, s: str) -> str:
        mid_ste= ""
        resoult = ""
        s_list = [x for x in list(s)]
        cycle = 0
        for x in range(len(s_list)-1,-1,-1):
            if s_list[x] == "]":
                resoult = mid_ste + resoult
                mid_ste = ""
                cycle+=1

            if s_list[x] == "[":

                cycle-=1
            if 97<=ord(s_list[x])<=122:
                mid_ste = s_list[x]+ mid_ste
            if 48<=ord(s_list[x])<=57:
                mid_ste = int(s_list[x])*mid_ste
                resoult = mid_ste + resoult
                mid_ste = ""
        return resoult

# print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("3[a]2[bc]"))