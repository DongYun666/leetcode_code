# -*- codeing = utf-8 -*-
# @Time : 2021/10/30 20:13
# @Author : DongYun
# @File : 1286. 字母组合迭代器.py
# @Software : PyCharm
from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.index =-1
        self.resoult = list(combinations(characters,combinationLength))
    def next(self) -> str:
        self.index += 1
        if self.hasNext():
            return "".join((self.resoult)[self.index])
    def hasNext(self) -> bool:
        return False if self.index >= len(self.resoult) else True


# class CombinationIterator2:
#     def __init__(self, characters: str, combinationLength: int):
#         self.characters = characters
#         self.combinationLength = combinationLength
#     def next(self) -> str:
#
#     def hasNext(self) -> bool:
if __name__ == '__main__':
    resoult = CombinationIterator("abc",2)
    print(resoult.next())
    # print(resoult.hasNext())
    print(resoult.next())
    # print(resoult.hasNext())
    print(resoult.next())
    print(resoult.next())
    print(resoult.hasNext())