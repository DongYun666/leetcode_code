# -*- codeing = utf-8 -*-
# @Time : 2021/10/15 21:09
# @Author : DongYun
# @File : LinkList.py
# @Software : PyCharm
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create(list):
    head = ListNode(0)
    pre = head
    index = 0
    while index < len(list):
        new_head = ListNode(list[index])
        index+=1
        pre.next = new_head
        pre = new_head
    return head.next
def print_list(head):
    pre = head
    while pre:
        print(pre.val)
        pre = pre.next