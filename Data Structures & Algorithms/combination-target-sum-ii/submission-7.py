class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()

        res = []
        
        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                cur.append(nums[j])
                dfs(j+1,total+nums[j],cur)
                cur.pop()
        
        dfs(0,0,[])
        return res