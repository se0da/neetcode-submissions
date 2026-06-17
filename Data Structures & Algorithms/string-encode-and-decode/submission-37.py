class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1

            length = int(s[i:j]) 
            j += 1
            word = s[j:j+length]
            ans.append(word)
            i = j + length
        return ans
        