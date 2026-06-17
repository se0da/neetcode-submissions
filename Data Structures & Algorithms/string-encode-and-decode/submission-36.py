class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += (str(len(s))+ "#" + s)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            # 1. Read the number (length)
            while s[j].isdigit():
                j += 1
            
            length = int(s[i:j])  # convert digits to number
            
            # 2. Skip the '#'
            j += 1
            
            # 3. Extract the word
            word = s[j:j+length]
            ans.append(word)
            
            # 4. Move pointer forward
            i = j + length

        return ans

            