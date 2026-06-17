class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r-l)//2
            if self.isValid(piles, m, h):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

    def isValid(self, piles: List[int], mid: int, h: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/mid)
        return hours <= h
    