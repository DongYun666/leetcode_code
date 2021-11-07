# -*- codeing = utf-8 -*-
# @Time : 2021/10/25 10:48
# @Author : DongYun
# @File : 240.搜索二维矩阵2.py
# @Software : PyCharm
import bisect
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #太麻烦
        # def dfs(index_i,index_j,flag):
        #     if 0<=index_i<len(matrix) and 0<=index_j < len(matrix[0]):
        #         if matrix[index_i][index_j] == target:
        #             flag =  True
        #             return flag
        #         elif matrix[index_i][index_j]<target:
        #             if dfs(index_i,index_j+1):
        #
        #     else:
        #         flag = False
        #         return flag
        #dfs(0,0,False)

        '''
        使用暴力解决
        :param matrix:
        :param target:
        :return:
        '''
        for row in matrix:
            for ele in row:
                if ele == target:
                    return True
        ##未找到，返回False
        return False
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False

# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
# print(Solution().searchMatrix2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],100))
print(Solution().searchMatrix3([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))