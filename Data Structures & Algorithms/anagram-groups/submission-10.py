class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)

        answer = []
        for key in ans.keys():
            answer.append(ans.get(key))
        
        return answer
