# -*- codeing = utf-8 -*-
# @Time : 2021/10/22 20:48
# @Author : DongYun
# @File : 1475.商品折扣后的最终价格.py
# @Software : PyCharm
class Solution(object):
    def finalPrices(self, prices):
        for index,price in enumerate(prices):
            start = index+1
            while start!= len(prices):
                if prices[start]<prices[index]:
                    prices[index]-=prices[start]
                    break
                start+=1
        return prices
    def finalPrices2(self, prices):
        stack = []
        for i,p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                prices[stack.pop()] -= p
            stack.append(i)
        return prices
print(Solution().finalPrices2([8,4,6,2,3]))