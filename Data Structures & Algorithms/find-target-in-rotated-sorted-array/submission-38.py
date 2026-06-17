class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #finding pivot
        l, r = 0, len(nums) - 1
        while l < r:
             m = (l+r)//2
             if nums[m] < nums[r]:
                r = m
             else:
                l = m + 1 
        
        pivot = l
        l,r = 0, len(nums) - 1
        if pivot > 0 and nums[l] <= target <= nums[pivot-1]:
            r = pivot - 1
        else:
            l = pivot 
        
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1
