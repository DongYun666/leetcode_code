# -*- codeing = utf-8 -*-
# @Time : 2021/10/15 19:46
# @Author : DongYun
# @File : 38.外观数列.py
# @Software : PyCharm
class Solution:
    def countAndSay(self, n: int) -> str:
        resoult = ["1"]
        new_resoult = []

        ## 寻找重复的个数
        def find_next(resoult, start, num):
            count = 0
            while start <len(resoult) and resoult[start] == num:
                count += 1
                start += 1
            return count

        for i in range(n-1):
            while len(resoult) !=0:
                index = 0
                count = find_next(resoult, index, resoult[index])
                new_resoult.append(str(count))
                new_resoult.append(resoult[index])
                index += count
                resoult = resoult[index:]
            resoult = new_resoult
            new_resoult = []
        return "".join(resoult)

    def countAndSay2(self, n: int) -> str:
        prev = "1"
        for i in range(n - 1):
            curr = ""
            pos = 0
            start = 0

            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr

        return prev

# print(Solution().countAndSay(4))
print(Solution().countAndSay2(30))