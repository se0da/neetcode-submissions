class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans+=s+'.'
        return ans
    def decode(self, s: str) -> List[str]:
        char_list = list(s)
        strs = ''
        ans = []
        while(char_list):
            if char_list[0] == '.':
                ans.append(strs)
                char_list.pop(0)
                strs = ''
            else:
                strs+=char_list[0]
                char_list.pop(0)
        return ans