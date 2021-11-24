# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 16:03
# @Author : DongYun
# @File : 字母变数字的逆转.py
# @Software : PyCharm
def decode(str,i):
    if i == len(str):
        return 1
    if str[i] == '0':
        return 0
    if str[i] == '1':
        res = decode(str,i+1)
        if i+1 <len(str):
            res +=decode(str,i+2)
        return res
    if str[i] == '2':
        res = decode(str,i+1)
        if i+1<len(str) and '6' >= str[i+1] >= '0':
            res += decode(str , i+2)
        return res
    return decode(str , i+1)
def number(num):
    if num <= 0 :
        return False
    return decode(str(num),0)
