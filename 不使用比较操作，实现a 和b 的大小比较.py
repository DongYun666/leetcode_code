# -*- codeing = utf-8 -*-
# @Time : 2021/11/1 17:45
# @Author : DongYun
# @File : 不使用比较操作，实现a 和b 的大小比较.py
# @Software : PyCharm
def bijiao(a,b):

    return ((a+(~b+1))>>31)

print(bijiao(3,2))


