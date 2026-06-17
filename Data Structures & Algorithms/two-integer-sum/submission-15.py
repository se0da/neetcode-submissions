class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, x in enumerate(nums):
            y = target - x
            if len(prevMap.keys()) != 0 and prevMap.get(y) is not None:
                return [prevMap.get(y), i]
            
            prevMap[x] = i
        
        return None