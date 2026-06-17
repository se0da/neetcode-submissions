class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                cur.append(nums[j])
                dfs(cur, total+nums[j], j)
                cur.pop()
        dfs([],0,0)
        return res