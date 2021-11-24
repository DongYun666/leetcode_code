# -*- codeing = utf-8 -*-
# @Time : 2021/11/14 20:00
# @Author : DongYun
# @File : 1450.在既定时间做作业的学生人数.py
# @Software : PyCharm
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for index in range(len(startTime)):
            if startTime[index] <= queryTime and endTime[index] >= queryTime:
                count += 1
        return count

    def busyStudent1(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return [startTime[i] <= queryTime and endTime[i] >= queryTime for i in range(len(startTime))].count(True)


print(Solution().busyStudent1([2, 90, 61, 50, 99, 1], [31, 93, 99, 79, 99, 24], 50))
