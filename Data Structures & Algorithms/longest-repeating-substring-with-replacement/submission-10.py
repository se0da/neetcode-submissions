class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        res = 0
        my_m = {}
        l = 0
        for r in range(len(s)):
            my_m[s[r]] = my_m.get(s[r],0)+1
            maxf = max(maxf, my_m.get(s[r]))
            while (r-l+1)-maxf > k:
                my_m[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res