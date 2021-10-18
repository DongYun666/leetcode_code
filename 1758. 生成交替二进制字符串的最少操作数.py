# -*- codeing = utf-8 -*-
# @Time : 2021/10/16 20:25
# @Author : DongYun
# @File : 1758. 生成交替二进制字符串的最少操作数.py
# @Software : PyCharm
class Solution:
    def minOperations(self, s: str) -> int:
        new_s1="01"*(len(s)//2)+"0"*(len(s)%2)
        new_s2="10"*(len(s)//2)+"1"*(len(s)%2)
        def count_differ(new_s):
            count = 0
            for index,i in enumerate(s):
                if i != new_s[index]:
                    count+=1
            return count
        return min(count_differ(new_s1),count_differ(new_s2))
    def minOperations2(self, s: str) -> int:
        zero,one= 0,0
        flag = '1'
        for  c in bytearray(s,encoding="utf-8"):
            print(c)
            if c == flag:
                zero+=1
            else:
                one+=1
            if flag == '0':
                flag = '1'
            else:
                flag = '0'
        return min(zero, one);
    def minOperations3(self, s: str) -> int:
        n,cnt1,cnt2=len(s),0,0
        for i in range(n):
            if int(s[i])%2!=i%2:
                cnt1+=1
            else:
                cnt2+=1
        return min(cnt1,cnt2)
# print(Solution().minOperations("1111"))
print(Solution().minOperations3("1111"))
