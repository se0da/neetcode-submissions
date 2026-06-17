class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0
        max1 = 0
        for r in range(len(s)):
            count[s[r]] = 1+count.get(s[r],0)
            max1 = max(max1, count[s[r]])

            if(r - l + 1) - max1 > k:
                count[s[l]] -= 1
                l += 1
            
        return (r - l + 1)