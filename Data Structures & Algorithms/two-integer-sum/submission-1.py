class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for var in range(len(nums)):
            find = target - nums[var]
            if(find in myMap):
                return (myMap[find], var)
            else:
                myMap[nums[var]] = var
