# -*- codeing = utf-8 -*-
# @Time : 2021/10/31 20:50
# @Author : DongYun
# @File : 剑指 Offer 12. 矩阵中的路径.py
# @Software : PyCharm
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = [[False for i in range(len(board[0]))] for j in range(len(board))]
        # def dfs()
        return flag

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))