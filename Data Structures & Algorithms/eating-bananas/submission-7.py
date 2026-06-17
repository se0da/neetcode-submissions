class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res
        while l <= r:
            mid = l + (r-l)//2
            if self.isValid(piles,mid,h):
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        return res

    def isValid(self, piles: List[int], mid: int, h: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/mid)

        return hours <= h