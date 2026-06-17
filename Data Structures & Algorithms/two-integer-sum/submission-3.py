class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in my_map:
                return [my_map[tmp], i]
            else:
                my_map[nums[i]] = i
            
        