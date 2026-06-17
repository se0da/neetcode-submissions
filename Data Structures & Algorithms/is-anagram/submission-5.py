class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}
        for v in s:
            my_map[v] = my_map.get(v, 0) + 1
        
        my_sec_map = {}
        for v in t:
            my_sec_map[v] = my_sec_map.get(v,0) + 1
        
        if my_map == my_sec_map:
            return True
        
        return False
        