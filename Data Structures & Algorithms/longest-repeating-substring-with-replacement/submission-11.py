class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        my_map = {}
        max_len = 0
        for r in range(len(s)):
            my_map[s[r]] = my_map.get(s[r],0)+1
            curr_len = r-l+1
            max_freq = max(max_freq, my_map[s[r]])
            while max_freq + k < curr_len:
                curr_len -= 1
                my_map[s[l]] = my_map.get(s[l])-1
                l += 1
            max_len = max(max_len, curr_len)
        
        return max_len