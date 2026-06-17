class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            char_map = [0] * 26
            for c in s:
                char_map[ord(c)-ord('a')] += 1
            res[tuple(char_map)].append(s)
            
        return res.values()
