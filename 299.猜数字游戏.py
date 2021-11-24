# -*- codeing = utf-8 -*-
# @Time : 2021/11/8 19:50
# @Author : DongYun
# @File : 299.猜数字游戏.py
# @Software : PyCharm
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        new_secret = list(secret)
        count_A = 0
        count_B = 0
        for index,ch in enumerate(guess):
            if guess[index] == new_secret[index] :
                new_secret[index] = "#"
                count_A+=1
            elif new_secret[index][0] =="#" and  guess[index]== new_secret[index][1]:
                count_A +=1
                if  new_secret.count(ch) == 0:
                    count_B -=1
            else:
                if ch in new_secret:
                    new_secret["".join(new_secret).find(ch)] = "#"+ch
                    count_B+=1
        return str(count_A)+"A"+str(count_B)+"B"
print(Solution().getHint("1","1"))
# str = "10"
