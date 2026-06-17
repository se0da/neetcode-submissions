class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        done = set()  
        curr = set()  

        def dfs(crs):
            if crs in done:
                return True
            if crs in curr:
                return False
            curr.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            curr.remove(crs)
            done.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
