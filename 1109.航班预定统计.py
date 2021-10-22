
# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 19:39
# @Author : DongYun
# @File : 1109.航班预定统计.py
# @Software : PyCharm
import numpy as np
class Solution(object):
    #超时
    def corpFlightBookings(self, bookings, n):
        resoult = [0]*n
        print(resoult)
        for booking in bookings:
            # a = resoult[(booking[0]-1):(booking[1]-1)]
            b =  [0]*(booking[0]-1)+[booking[2]]*(booking[1]-booking[0]+1)+[0]*(n-booking[1])
            resoult = np.sum([resoult , b], axis=0).tolist()
        return resoult
    def corpFlightBookings2(self, bookings, n):
        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums


print(Solution().corpFlightBookings2([[1,2,10],[2,2,15]],2))
# print([1,2,3]+[1,1,1])