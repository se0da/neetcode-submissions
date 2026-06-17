class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if(k in myMap):
                return (myMap[k], i)
            else:
                myMap[nums[i]] = i

