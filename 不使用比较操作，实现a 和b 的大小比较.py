# -*- codeing = utf-8 -*-
# @Time : 2021/11/1 17:45
# @Author : DongYun
# @File : 不使用比较操作，实现a 和b 的大小比较.py
# @Software : PyCharm
def flip(n):
    return n ^ 1
def sign(n):
    return flip((n >> 31) & 1)
def bijiao(a,b):
    c = a - b
    scA = sign(c)
    scB = flip(scA)
    return a * scA + b * scB
print(bijiao(1,3))


