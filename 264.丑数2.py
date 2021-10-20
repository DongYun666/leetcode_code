# -*- codeing = utf-8 -*-
# @Time : 2021/10/19 21:09
# @Author : DongYun
# @File : 264.丑数2.py
# @Software : PyCharm

l = []
for x in range(100):
    #判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x <2:
        continue
    for i in range(2,x):
        if x % i == 0:
            break
        else:
            l.append(x)
print(l)