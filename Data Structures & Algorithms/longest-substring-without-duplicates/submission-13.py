class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        cur = set()
        for r in range(len(s)):
            if s[r] in cur:
                while s[r] in cur:
                    cur.remove(s[l])
                    l += 1
            cur.add(s[r])
            res = max(res, len(cur))
        
        return res
        