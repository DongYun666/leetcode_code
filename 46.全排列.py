# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 15:02
# @Author : DongYun
# @File : 46.全排列.py
# @Software : PyCharm
class Solution:
    def permute(self, nums):
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            visit = [0 for i in range(26)]
            for i in range(first, n):
                # 动态维护数组
                if not visit[ord(nums[i])-ord('a')]:
                    visit[ord(nums[i])-ord('a')] = nums[i]
                    nums[first], nums[i] = nums[i], nums[first]
                    # 继续递归填下一个数
                    backtrack(first + 1)
                    # 撤销操作
                    nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
print(Solution().permute(['a','b','c','a']))




