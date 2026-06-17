class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, total ,cur):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i,len(nums)):
                if total + nums[j] > target:
                    return
                
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                cur.append(nums[j])
                dfs(j+1,total+nums[j],cur)
                cur.pop()
        dfs(0,0,[])
        return res