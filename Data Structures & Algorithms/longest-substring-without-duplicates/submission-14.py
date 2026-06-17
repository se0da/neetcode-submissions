class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_s = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in my_s:
                my_s.remove(s[l])
                l+=1
            my_s.add(s[r])
            res = max(res, len(my_s))
        return res
