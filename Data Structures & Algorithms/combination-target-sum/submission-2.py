class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                cur.append(nums[j])
                dfs(j,nums[j]+total,cur)
                cur.pop()
            
        dfs(0,0,[])
        return res