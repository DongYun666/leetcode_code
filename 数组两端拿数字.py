# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 15:29
# @Author : DongYun
# @File : 数组两端拿数字.py
# @Software : PyCharm

def whowin(arr):
    if len(arr)<1:
        return 0
    return max(first(arr,0,len(arr)-1),after(arr,0,len(arr)-1))
def first(arr,i,j):
    if i == j:
        return arr[i]
    return max(arr[i]+after(arr,i+1,j),arr[j]+after(arr,i,j-1))
def after(arr,i,j):
    if i == j :
        return 0
    return min(first(arr,i+1,j),first(arr,i,j-1))

print(whowin([1,4,10,2]))