class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for var in nums:
            if var in mySet:
                return True
            else:
                mySet.add(var)
            
        return False