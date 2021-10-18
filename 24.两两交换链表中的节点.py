# -*- codeing = utf-8 -*-
# @Time : 2021/10/15 20:28
# @Author : DongYun
# @File : 24.两两交换链表中的节点.py
# @Software : PyCharm
from warehouse import LinkList as ll
def swapPairs(head: ll.ListNode) -> ll.ListNode:
    new_head = ll.ListNode(0)
    new_head.next = head
    temp = new_head
    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
    return new_head.next

if __name__ == '__main__':
    head = ll.create([1,2,3,4,5,6,7])
    ll.print_list(swapPairs(head))
