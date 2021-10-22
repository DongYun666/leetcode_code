# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 21:05
# @Author : DongYun
# @File : 2.两数相加.py
# @Software : PyCharm
# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode() {}
#  *     ListNode(int val) { this.val = val; }
#  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
#  * }
#  */
# class Solution {
#     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
#  ListNode Ne=new ListNode(0,null);
#         ListNode ans=Ne;
#         int flag=0;
#         while(l1!=null && l2!=null){
#             int k=l1.val+l2.val+flag;
#             flag=0;
#             if(k>=10){
#                 k=k-10;
#                 flag=1;
#             }
#             ListNode t=new ListNode(k);
#             Ne.next=t;
#             Ne=Ne.next;
#             l1=l1.next;
#             l2=l2.next;
#         }
#         while(l1!=null){
#             int k=l1.val+flag;
#             flag=0;
#             if(k>=10){
#                 k=k-10;
#                 flag=1;
#             }
#             ListNode t=new ListNode(k);
#             Ne.next=t;
#             Ne=Ne.next;
#             l1=l1.next;
#         }
#         while(l2!=null){
#             int k=l2.val+flag;
#             flag=0;
#             if(k>=10){
#                 k=k-10;
#                 flag=1;
#             }
#             ListNode t=new ListNode(k);
#             Ne.next=t;
#             Ne=Ne.next;
#             l2=l2.next;
#         }
#         if(flag==1){
#             ListNode t=new ListNode(1);
#             Ne.next=t;
#         }
#         return ans.next;
#     }
# }