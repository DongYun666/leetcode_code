# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 15:44
# @Author : DongYun
# @File : 不适用额外的空间，实现栈逆序.py
# @Software : PyCharm
class Stack(object):
    # 初始化栈为空列表
    def __init__(self,arr):
        self.items = arr

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        return self.items.pop()


def getBottom(arr):
    resoult = arr.pop()
    if arr.size() < 1:
        return resoult
    else:
        last = getBottom(arr)
        arr.push(resoult)
        return last

def Reverse(arr):
    if arr.size()<2:
        return arr
    keep = getBottom(arr)
    Reverse(arr)
    arr.push(keep)
print(Reverse(Stack([1,2,3,4,5])))









