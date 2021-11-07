# -*- codeing = utf-8 -*-
# @Time : 2021/11/1 8:49
# @Author : DongYun
# @File : Sunday算法.py
# @Software : PyCharm
def sunday_find(src, dst):
    len_src = len(src)
    len_dst = len(dst)
    i = 0
    p=0
    while i < len_src - len_dst + 1:
        flag = 0
        shift = len_dst
        for j in range(len_dst-1,-1,-1):
            if src[i+j] != dst[j]:
                flag = -1
                break
            # if i+shift < len_src and src[i+shift] == dst[j]:
            #     p = j
        if flag == 0:
            return i
        p = dst.rfind(src[i+shift])
        if p == -1:
            shift = len_dst + 1
        else:
            shift = len_dst - p
        i = i + shift
    return -1


if __name__ == "__main__":
    text = "here_examplfe_v_example"
    pattern = "plea"
    pos = sunday_find(text, pattern)
    print(pos)
