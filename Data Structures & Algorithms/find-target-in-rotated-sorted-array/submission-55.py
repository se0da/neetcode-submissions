class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l+(r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        rotation = l
            
        if nums[rotation] <= target <= nums[len(nums)-1]:
            l, r = rotation, len(nums)-1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
        
        else:
            l, r = 0, rotation
            while l <= r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
        
        return -1
