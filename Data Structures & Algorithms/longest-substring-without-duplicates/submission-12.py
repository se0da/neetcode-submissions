class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])
            longest = max(longest, len(cur))
        
        return longest
