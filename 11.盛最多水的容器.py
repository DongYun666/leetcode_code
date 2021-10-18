# -*- codeing = utf-8 -*-
# @Time : 2021/9/29 19:44
# @Author : DongYun
# @File : 11盛最多水的容器.py
# @Software : PyCharm
class Solution:
    def maxArea(self,height: list[int]) ->int:
        start,end,area = 0,len(height)-1,0
        while start != end:
            area = max(area,(end-start)*min(height[start],height[end]))
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return area
print(Solution().maxArea([4,3,2,1,4]))