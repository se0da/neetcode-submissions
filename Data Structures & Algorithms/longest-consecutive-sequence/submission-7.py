class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        res = 0
        for n in nums:
            if n-1 in n_set:
                continue
            
            length = 0
            while n+length in n_set:
                length += 1
            res = max(res, length)
        return res