# -*- codeing = utf-8 -*-
# @Time : 2021/10/20 9:56
# @Author : DongYun
# @File : 1433.检查一个字符串是否可以打破另一个字符串.py
# @Software : PyCharm
class Solution(object):
    # def checkIfCanBreak(self, s1, s2):
    #     flag1,flag2 = False,False
    #     def s_2_nums(s):
    #         ans = []
    #         for ch in s:
    #             ans.append(ord(ch)-ord('a'))
    #         return ans
    #     new_s1 = sorted(s_2_nums(s1))
    #     new_s2 = sorted(s_2_nums(s2))
    #     for i in range(len(new_s1)):
    #         if new_s1[i]>=new_s2[i]:
    #             flag1 = True
    #         else:
    #             flag1 = False
    #             break
    #     for i in range(len(new_s2)):
    #         if new_s2[i]>=new_s1[i]:
    #             flag2 = True
    #         else:
    #             flag2 = False
    #             break
    #     return flag1 or flag2

    #改进：
        def checkIfCanBreak(self, s1, s2):
            ch_count1,ch_count2 = [0]*26,[0]*26
            for ch in s1:
                ch_count1[ord(ch)-ord('a')]+=1
            for ch in s2:
                ch_count2[ord(ch)-ord('a')]+=1
            flag =0
            for i in range(25,-1,-1):
                if ch_count1[i] == ch_count2[i]:
                    continue
                if ch_count1[i]>ch_count2[i]:
                    if flag == 2:
                        return False
                    flag = 1
                    ch_count1[i - 1] += ch_count1[i] - ch_count2[i]
                else:
                    if flag == 1:
                        return False
                    flag = 2
                    ch_count2[i - 1] += ch_count2[i] - ch_count1[i]
            return True

print(Solution().checkIfCanBreak("abc","xya"))