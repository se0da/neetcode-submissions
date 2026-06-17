class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1
            
            num = int(s[i:j])
            j += 1
            word = s[j:j+num]
            ans.append(word)
            i = j + num
        return ans 