# -*- codeing = utf-8 -*-
# @Time : 2021/11/10 9:25
# @Author : DongYun
# @File : 495.提莫攻击.py
# @Software : PyCharm
from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_count = 0
        for index,time in enumerate(timeSeries):
            if index  <len(timeSeries)-1:
                # 中毒期间二次中毒
                if time + duration > timeSeries[index+1]:
                    time_count = time_count+(timeSeries[index+1]-time)
                else:
                    time_count +=duration
        time_count+=duration
        return time_count


    def findPoisonedDuration2(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0
        last_time = timeSeries[0]
        for i in timeSeries[1:]:
            if i - last_time >= duration:
                total_time += duration
            else:
                total_time += i - last_time
            last_time = i
        return total_time + duration


print(Solution().findPoisonedDuration2([1,2,4],2))



