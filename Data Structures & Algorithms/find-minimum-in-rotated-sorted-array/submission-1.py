class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = left+((right-left)//2)
            #if the middle value is greater than right then pivot is right 
            #update left to be mid + 1
            if nums[mid] > nums[right]:
                left = mid + 1
            #if middle value is less than or equal to left than the pivot is left
            elif nums[mid] <= nums[right]:
                right = mid

        return nums[left]

