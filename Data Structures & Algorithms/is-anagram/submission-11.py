class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}
        for i, n in enumerate(s):
            map1[n] = map1.get(n,0)+1
        for i, n in enumerate(t):
            map2[n] = map2.get(n,0)+1
        
        return map1 == (map2)

