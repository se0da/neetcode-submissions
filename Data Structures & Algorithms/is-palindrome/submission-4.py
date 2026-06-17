class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        def isAlphaNum(c):
            return (ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
        
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
            
        return True