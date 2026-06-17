class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i in range(len(nums)):
            tmp = target - nums[i]

            if tmp in myMap:
                return [myMap[tmp], i]
            
            else:
                myMap[nums[i]] = i
            
        