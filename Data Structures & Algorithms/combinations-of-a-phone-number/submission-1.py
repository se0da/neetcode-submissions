class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = ""

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            nonlocal cur
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for v in digitToChar[digits[i]]:
                cur += v
                dfs(i+1)
                cur=cur[:-1]
            
        if digits:
            dfs(0)
        return res