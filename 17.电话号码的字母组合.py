# -*- codeing = utf-8 -*-
# @Time : 2021/10/6 20:32
# @Author : DongYun
# @File : 17.电话号码的字母组合.py
# @Software : PyCharm
import math
math.__file__
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        resoult = []
        nums_letter = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        def backtrack(letter,next_digits):
            if len(next_digits) == 0:
                resoult.append(letter)
            else :
                for num in nums_letter(next_digits[0]):
                    backtrack(num+letter,next_digits[1:])
        backtrack('',digits)
        return resoult

    def test(self,digits):
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res

# print(Solution().letterCombinations(digits='23'))
# print(Solution().test('23'))

math.__file__
print(math.factorial(100))