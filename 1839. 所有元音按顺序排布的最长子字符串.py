# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 19:47
# @Author : DongYun
# @File : 1839. 所有元音按顺序排布的最长子字符串.py
# @Software : PyCharm
class Solution:
    # 判别次数太多
    # def longestBeautifulSubstring(self, word: str) -> int:
    #     flag = False
    #     if len(word)==1:
    #         return 0
    #     w = 'a'.encode()
    #     count = 0
    #     max_count = 0
    #     for ch in word:
    #         new_ch = ch.encode()
    #         if new_ch>=w:
    #             count+=1
    #             w = new_ch
    #             if new_ch == 'a'.encode():
    #                 flag = True
    #             if new_ch == 'u'.encode():
    #                 max_count = max(max_count,count)
    #         else:
    #             flag = False
    #             if w == 'u'.encode():
    #                 max_count = max(max_count,count)
    #                 flag = True
    #             count = 1
    #             w = 'a'.encode()
    #     return max_count if flag else 0
    #
    #
    def longestBeautifulSubstring2(self, word: str) -> int:
        if len(word) < 5:
            return 0
        res = 0
        rlen = 1
        vowel = 1 #用于统计出现的种类次数，只有当前大于前一个时，才加一
        for i in range(1,len(word)):
            if word[i]>=word[i-1]:
                rlen+=1
            if word[i]>word[i-1]:
                vowel+=1
            if word[i]<word[i-1]:
                rlen=1
                vowel=1
            if vowel==5:
                res=max(rlen,res)
        return res
    #使用状态机

    TRANSIT = {
        ("a", "e"), ("e", "i"), ("i", "o"), ("o", "u"),
        ("a", "a"), ("e", "e"), ("i", "i"), ("o", "o"), ("u", "u"),
        ("x", "a"), ("e", "a"), ("i", "a"), ("o", "a"), ("u", "a"),
    }

    def longestBeautifulSubstring3(self, word: str) -> int:
        cur, ans = 0, 0
        status = "x"
        for ch in word:
            if (status, ch) in Solution.TRANSIT:
                if status != "a" and ch == "a":
                    cur = 1
                else:
                    cur = cur + 1
                status = ch
            else:
                cur = 0
                status = "x"
            if status == "u":
                ans = max(ans, cur)
        return ans



print(Solution().longestBeautifulSubstring3("aaeiou"))
# print("abcde"[-1])