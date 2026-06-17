class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            m = (l+r)//2
            cur = 0
            for p in piles:
                cur += math.ceil(p/m)
            if cur <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res

