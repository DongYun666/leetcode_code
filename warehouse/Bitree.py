# -*- codeing = utf-8 -*-
# @Time : 2021/11/16 16:35
# @Author : DongYun
# @File : BiTree.py
# @Software : PyCharm
class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.is_None = False

    def __str__(self):
        return str(self.data)


class BiTree:
    def __init__(self, list_node = [],root=None):
        if len(list_node) == 0:
            self.root = root
        else:
            self.root = root
            for i in list_node:
                self.add(i)
    def add(self, item):
        node = Node(item)
        if item == None:
            node.is_None = True
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):
        # 找到item的父节点
        if self.root.data == item:
            return None
        q = [self.root]
        while q:
            pop_node = q.pop(0)
            if pop_node.left and pop_node.left.data == item:
                return pop_node
            elif pop_node.right and pop_node.right.data == item:
                return pop_node
            else:
                if pop_node.left is not None:
                    q.append(pop_node.left)
                if pop_node.right is not None:
                    q.append(pop_node.right)
        return None

    def delete(self, item):
        '''
        从二叉树中删除一个元素
        先获取 待删除节点 item 的父节点
        如果父节点不为空，
            判断 item 的左右子树
            如果左子树为空，那么判断 item 是父节点的左孩子，还是右孩子，如果是左孩子，将父节点的左指针指向 item 的右子树，反之将父节点的右指针指向 item 的右子树
            如果右子树为空，那么判断 item 是父节点的左孩子，还是右孩子，如果是左孩子，将父节点的左指针指向 item 的左子树，反之将父节点的右指针指向 item 的左子树
            如果左右子树均不为空，寻找右子树中的最左叶子节点 x ，将 x 替代要删除的节点。
        删除成功，返回 True
        删除失败, 返回 False

        '''
        if self.root is None:  # 如果根为空，就什么也不做
            return False

        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.data == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.data == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.data == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.data == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def preorder(self, root):
        if not root:
            return []
        result = [root.data]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorder(self, root):
        if not root:
            return []
        result = [root.data]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self, root):
        if not root:
            return []
        result = [root.data]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result

    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.data]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.data)
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.data)
        return res
    def get_root(self):
        return self.root

    def morrisPre(self,head):
        resoult = []
        if not head:
            return
        cur = head
        mostRight = None
        while cur:
            mostRight = cur.left;
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right
                if not mostRight.right:
                    resoult.append(cur.data)
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None
                    # print(cur.data,end=" ")
            else:
                resoult.append(cur.data)
            cur = cur.right
        return resoult

    def morrisIn(self,head):
        resoult = []
        if not head:
            return
        cur = head
        mostRight = None
        while cur:
            mostRight = cur.left;
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right
                if not mostRight.right:
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None
            # print(cur.data, end=" ")
            resoult.append(str(cur.data))
            cur = cur.right
        return resoult
    def morrisPos(self,head):
        resoult = []
        if not head:
            return
        cur = head
        mostRight = None

        def printEdge(node):
            tail = reverseEdge(node)
            cur = tail
            while cur:
                resoult.append(cur.data)
                # print(cur.data,end=" ")
                cur = cur.right
            reverseEdge(tail)

        def reverseEdge(node):
            pre = None
            next = None
            while node:
                next = node.right
                node.right = pre
                pre = node
                node = next
            return pre
        while cur:
            mostRight = cur.left;
            if mostRight:
                while  mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right
                if not mostRight.right:
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None
                    printEdge(cur.left)
                    # print()
            cur = cur.right
        printEdge(head)
        return resoult













