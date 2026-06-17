class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        curr_len = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in my_set:
                my_set.add(s[r])
                curr_len += 1
            
            else:
                while s[r] in my_set:
                    my_set.remove(s[l])
                    l += 1
                    curr_len -= 1
                my_set.add(s[r])
                curr_len += 1
            res = max(res,curr_len)
        return res
                

            