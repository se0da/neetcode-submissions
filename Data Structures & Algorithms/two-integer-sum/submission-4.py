class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, x in enumerate(nums):
            var = target - x
            if var in my_map:
                return [my_map[var], i]
            my_map[x] = i