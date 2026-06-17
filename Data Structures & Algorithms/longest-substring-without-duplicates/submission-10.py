class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        my_set = set()
        l = r = 0
        while r < len(s):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            
            my_set.add(s[r])
            longest = max(longest, len(my_set))
            r += 1
        
        return longest
