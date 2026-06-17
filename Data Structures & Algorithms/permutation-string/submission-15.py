class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s1_char = [0] * 26

        for c in range(len(s1)):
            s1_char[ord(s1[c])-ord('a')] += 1

        print(s1_char)

        curr_window = [0] * 26

        for c in range(len(s1)):
            curr_window[ord(s2[c])-ord('a')] += 1
        
        l, r = 0, len(s1)-1
        
        if curr_window == s1_char: 
            return True

        while r < len(s2)-1:
            r += 1
            curr_window[ord(s2[r])-ord('a')] += 1
            curr_window[ord(s2[l])-ord('a')] -= 1
            l += 1
            print(curr_window)
            if curr_window == s1_char: 
                return True

        return False