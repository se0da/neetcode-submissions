class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        ans = 0
        
        for num in nums:
            if num-1 not in my_set:
                tmp = num
                consec = 1
                while tmp+1 in my_set:
                    tmp += 1 
                    consec += 1
                ans = max(ans, consec)
            
        return ans

