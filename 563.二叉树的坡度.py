# -*- codeing = utf-8 -*-
# @Time : 2021/11/18 20:39
# @Author : DongYun
# @File : 563.二叉树的坡度.py
# @Software : PyCharm
from warehouse.Bitree import Node,BiTree
class Solution:
    def __init__(self):
        self.resoult = 0
    def findTilt(self, root: Node) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.resoult += abs(left-right)
            return left+right+root.data
        dfs(root)
        return self.resoult

if __name__ == '__main__':
    bitree = BiTree([4,None,2,9,3,5,None,7])
    print(bitree.inorder(bitree.get_root()))
    print(Solution().findTilt(bitree.get_root()))