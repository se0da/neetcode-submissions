class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for v in nums:
                if v not in curr:
                    curr.append(v)
                    dfs()
                    curr.pop()

        dfs()        
        return res