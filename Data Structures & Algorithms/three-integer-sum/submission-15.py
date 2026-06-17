class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums)-2:

            j = i + 1
            k = len(nums) - 1
            target = -nums[i] 

            while j < k:
                total = nums[j] + nums[k] 
                if total == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
            
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1 
            
        return ans
