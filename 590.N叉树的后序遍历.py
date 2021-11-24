# -*- codeing = utf-8 -*-
# @Time : 2021/11/14 19:28
# @Author : DongYun
# @File : 590.N叉树的后序遍历.py
# @Software : PyCharm
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> List[int]:
        resoult  = []
        def post(root:Node):
            if root is None:
                return
            for children in root.children:
                post(children)
            resoult.append(root.val)
        post(root)
        return resoult


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #保存节点值
        result = []
        #后序遍历
        def pre_order(root):
            #跟节点非空入队列递归遍历
            if root:
                #递归遍历
                for node in root.children:
                    pre_order(node)
                #节点值入队列
                result.append(root.val)
        pre_order(root)
        return result


print(Solution().postorder([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]))