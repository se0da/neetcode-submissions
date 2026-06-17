class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [[] for _ in range(len(nums))]
        pre, post = 1, 1
        for n in range(len(nums)):
            output[n] = pre
            pre *= nums[n]
        
        for n in range(len(nums)-1, -1, -1):
            output[n] *= post
            post *= nums[n]
        
        return output
