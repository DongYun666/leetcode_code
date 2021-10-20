# -*- codeing = utf-8 -*-
# @Time : 2021/10/19 19:36
# @Author : DongYun
# @File : 212.添加与搜索单词.py
# @Software : PyCharm
class trid:
    #对字典树的变形，不存储值，只存储
    def __init__(self):
        self.isEnd = False
        self.value = [None]*26
        self.children = [None]*26
    def insert(self,word):
        node = self
        for ch in word:
            ch = ord(ch)-ord('a')
            if not node.children[ch]:
                node.children[ch] = trid()
                node.value[ch] = chr(97+ch)
                print(node.value)
            node = node.children[ch]
        node.isEnd = True

class WordDictionary:

    def __init__(self):
        self.tridRoot = trid()
    def addWord(self) ->None:
        for word in ["abcd","abce","bcdf","fghj","jikl"]:
            self.tridRoot.insert(word)
    def search(self, word: str)-> bool:
        def dfs(index: int, node: trid) ->bool:
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch!='.':
                child = node.children[ord(ch)-ord('a')]
                if child is not None and dfs(index+1,child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(index+1,child):
                        return True
            return False
        return dfs(0,self.tridRoot)
if __name__ == '__main__':
    ans = WordDictionary()
    ans.addWord()
    print(ans.search(".bcd"))

#
#     def search(self, word: str) -> bool: