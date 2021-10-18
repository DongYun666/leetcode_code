# -*- codeing = utf-8 -*-
# @Time : 2021/10/18 10:11
# @Author : DongYun
# @File : 804.唯一莫尔斯密码词.py
# @Software : PyCharm
from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dict_words = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        ans = set()
        for word in words:
            resoult = ""
            for w in word:
                resoult+=dict_words[ord(w)-ord('a')]
            ans.add(resoult)
        return len(ans)

print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
