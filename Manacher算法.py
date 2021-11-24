# -*- codeing = utf-8 -*-
# @Time : 2021/11/8 16:24
# @Author : DongYun
# @File : Manacher算法.py
# @Software : PyCharm
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]
print(Solution().longestPalindrome("abcscbabcabbac"))


def maxLc(str):
    if str or len(str) ==0:
        return 0
    str + "#"
    RArr = [0 for i in range(len(str))]  # 回文半径数组
    C,R = -1,-1
    resoult = float("inf")
    for i in range(len(str)):
        #对于4种情况，
        RArr[i] = min(RArr[2*C-i],R-i) if R > i else 1
        while i + RArr[i] <len(str) and i - RArr[i] >-1:
            if str[i+RArr[i]] == str[i - RArr[i]]:
                RArr[i]+=1
            else:
                break
        if i + RArr[i] > R:
            R = i + RArr[i]
            C = i
        resoult = max(resoult,RArr[i])
    return resoult-1  # 正好是resoult -1
# print(maxLc("abcscbabcabbac"))
