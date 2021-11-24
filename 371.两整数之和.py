# -*- codeing = utf-8 -*-
# @Time : 2021/10/27 21:09
# @Author : DongYun
# @File : 371.两整数之和.py
# @Software : PyCharm
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         # if a < 0 and b>0:
#         #     a = ~a+1
#         # if b < 0 and a>0:
#         #     b = ~b+1
#         while b != 0 :
#             a, b = a^b , (a & b)<<1
#         return a
# print(Solution().getSum(20,30))


MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1
def getSum2( a: int, b: int) -> int:
    a %= MASK1
    b %= MASK1
    while b != 0:
        carry = ((a & b) << 1) % MASK1
        a = (a ^ b) % MASK1
        b = carry
    if a & MASK2:  # 负数
        return ~((a ^ MASK2) ^ MASK3)
    else:  # 正数
        return a

print(getSum2(-2,3))


def add(a,b):
    sum = 0
    while b!= 0:
        sum = a ^ b
        b = (a & b) << 1
        a = sum
    return sum
print(add(2,3))



def negNum(n):
    return getSum2(~n,1)
def minus(a,b):
    return getSum2(a,negNum(b))

# print(minus(3,2))
# print(2 << 1)


def multi(a,b):
    flag_b = b
    res = 0
    while b != 0:
        res = getSum2(res,a)
        if b < 0:
            b = minus(b,-1)
        else:
            b = minus(b,1)
    return res if flag_b>0 else -res

print(multi(4,-5))

