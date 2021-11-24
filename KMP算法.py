# -*- codeing = utf-8 -*-
# @Time : 2021/11/24 20:12
# @Author : DongYun
# @File : KMP算法.py
# @Software : PyCharm
def get_next(t):
    next = [0 for i in range(len(T))]
    i=0
    j=-1
    next[0]=-1
    while i<len(t)-1:
        if j==-1 or t[i]==t[j]:
            i+=1
            j+=1
            next[i]=j
        else:
            j=next[j]
    return next
def KMP(S,T):
    i=0
    j=0
    next = get_next(T)
    while i<len(S) and j<len(T):
        if j==-1 or S[i]==T[j]:
            i+=1
            j+=1
        else:
            j= next[j]
    if i==len(S) and T[j-1]!=S[i-1]:
        return -1
    else:
        return i-j
S = input('母串:'+'')
T = input('子串:'+'')
pos=KMP(S,T)
print(pos)