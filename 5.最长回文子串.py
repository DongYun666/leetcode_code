# -*- codeing = utf-8 -*-
# @Time : 2021/9/28 19:46
# @Author : DongYun
# @File : 5.最长回文子串.py
# @Software : PyCharm
class Soultion:
    def longestPalindrome1(self,s: str) -> str:
        n = len(s)
        if(n<2):
            return s
        max_len = 1
        begin= 0
        dp =[[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for L in range(2,n+1):
            for i in range(n):
                j = L + i -1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i <3:
                        dp[i][j]=True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1>max_len:
                    max_len = j-i+1
                    begin =i
        return s[begin:begin+max_len]
    def expandAroundCenter(self,s,left,right):
        while left>=0 and right<len(s) and s[left] ==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    def longestPalindrome2(self,s: str) -> str:
        start , end = 0,0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s,i,i)
            left2, right2 = self.expandAroundCenter(s,i,i+1)
            if right1-left1 > end - start:
                start , end = left1 , right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]


print(Soultion().longestPalindrome2("abcddcbaefg"))
