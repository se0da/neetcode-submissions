class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for v in nums:
                if v not in cur:
                    cur.append(v)
                    dfs()
                    cur.pop()
            
        dfs()
        return res