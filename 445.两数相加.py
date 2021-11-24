# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 20:25
# @Author : DongYun
# @File : 445.两数相加.py
# @Software : PyCharm
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from warehouse.LinkList import SingleLinkList,Node
class Solution:
    def addTwoNumbers(self,l1: Node, l2: Node) -> SingleLinkList:
            s1, s2 = [], []
            while l1:
                s1.append(l1.elem)
                l1 = l1.next
            while l2:
                s2.append(l2.elem)
                l2 = l2.next
            ans = None
            carry = 0
            while s1 or s2 or carry != 0:
                a = 0 if not s1 else s1.pop()
                b = 0 if not s2 else s2.pop()
                cur = a + b + carry
                carry = cur // 10
                cur %= 10
                curnode = Node(cur)
                curnode.next = ans
                ans = curnode
            return ans
def travel(head):
    '''遍历整个列表'''
    cur = head
    while cur != None:
        print(cur.elem, end=' -> ')
        cur = cur.next
    print()
if __name__ == '__main__':
    l1 = SingleLinkList()
    l2 = SingleLinkList([2,4,6,2,4])
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.travel()
    l2.travel()
    s = Solution()
    travel(s.addTwoNumbers(l1.getHead(),l2.getHead()))










