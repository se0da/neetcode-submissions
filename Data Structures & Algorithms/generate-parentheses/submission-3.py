class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(closedN, openN):
            if closedN == openN == n:
                res.append("".join(cur))
                return
            
            if closedN < n:
                cur.append("(")
                dfs(closedN + 1, openN)
                cur.pop()
            
            if openN < closedN:
                cur.append(")")
                dfs(closedN, openN+1)
                cur.pop()
        
        dfs(0,0)
        return res
        
