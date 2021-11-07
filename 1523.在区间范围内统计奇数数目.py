class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return 0 if low % 2 == 0 else 1
        if low % 2 != 0:
            low-=1
        if high % 2 == 0:
            high-=1
        return int((high-low)/2)+1

print(Solution().countOdds(0,3))