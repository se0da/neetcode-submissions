class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, cur = [], []

        def backtrack():
            if len(cur) == n:
                res.append(cur.copy())
                return
            
            for x in nums:
                if x not in cur:
                    cur.append(x)
                    backtrack()
                    cur.pop()
            
        backtrack()
        return res

