class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        cur = set()
        done = set()
        adj_list = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs):
            if crs in cur:
                return False
            if crs in done:
                return True
            
            cur.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            cur.remove(crs)
            done.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res