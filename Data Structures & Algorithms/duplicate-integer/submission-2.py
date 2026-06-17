class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i in range(len(nums)):
            mySet.add(nums[i])
        
        if len(nums) == len(mySet):
            return False
        else:
            return True