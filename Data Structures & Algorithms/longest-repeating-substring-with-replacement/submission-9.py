class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        res = 0
        maxf = 0
        cur_map = {}
        for r in range(len(s)):                
            cur_map[s[r]] = cur_map.get(s[r],0)+1
            maxf = max(maxf, cur_map.get(s[r]))
            if (r-l+1) - maxf  <= k:
                res = max(res, r-l+1)
            else:
                while (r-l+1) - maxf > k:
                    cur_map[s[l]] -= 1
                    l += 1
                
        return res





