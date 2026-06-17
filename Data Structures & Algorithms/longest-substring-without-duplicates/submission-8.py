class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        res = 0
        l = r = 0

        while r < len(s):
            while (s[r] in my_set):
                my_set.remove(s[l])
                l+=1
            
            my_set.add(s[r])
            res = max(res, len(my_set))
            r += 1
        
        return res
