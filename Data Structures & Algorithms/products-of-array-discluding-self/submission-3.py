class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        output = [[] for _ in range(len(nums))]
        for i, n in enumerate(nums):
            output[i] = pre
            pre *= n

        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output