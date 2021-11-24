# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 9:36
# @Author : DongYun
# @File : 488.祖玛游戏.py
# @Software : PyCharm
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        res_board = []
        res_hand = list(hand)
        count = 1
        res_count = 0
        for index,b in enumerate(board):
            if index+1<len(board) and board[index+1] == board[index]:
                count+=1
            else:
                res_board.append(b)
                res_board.append(count)
                count = 1
        for i in range(0,len(res_board),2):
            if res_board[i] not in res_board[0:i]+res_board[i+1:] and res_board[i+1] ==2:
                if res_board[i] in res_hand:
                    res_hand.remove(res_board[i])
                    res_count+=1
                    res_board.remove()

        return res_board


print(Solution().findMinStep("RBYYBBRRB", "YRBGB"))