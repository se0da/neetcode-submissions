class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = defaultdict()
        for i in range(len(nums)):
            result = target - nums[i]
            if result in myMap:
                return [myMap[result], i]
            myMap[nums[i]] = i
        

