# -*- codeing = utf-8 -*-
# @Time : 2021/11/23 15:35
# @Author : DongYun
# @File : 派对的最大快乐值.py
# @Software : PyCharm
class Info():
    def __init__(self, height, dis):
        self.height = height
        self.dis = dis

def process(x):
    if not x.nexts: # 如果没有下属了，那么就返回自己的快乐值就好，第1个参数是来的快乐值，第2个参数是不来的快乐值
        return Info(x.happy, 0)
    lai = x.happy
    bu = 0
    for every in x.nexts:
        nextInfo = process(every)
        lai += nextInfo.bu
        bu += max(nextInfo.lai, nextInfo.bu)
    return Info(lai, bu)



