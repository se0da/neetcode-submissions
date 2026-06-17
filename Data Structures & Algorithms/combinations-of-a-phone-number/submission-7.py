class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        cur = []
        res = []


        def dfs(i):
            if len(cur) == len(digits):
                res.append("".join(cur.copy()))
                return
            
            for v in digitToChar[digits[i]]:
                cur.append(v)
                dfs(i+1)
                cur.pop()
        
        dfs(0)
        return res if digits else []

