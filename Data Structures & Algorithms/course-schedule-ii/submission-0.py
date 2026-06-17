class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        my_map = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            my_map[crs].append(pre)
        
        done, curr = set(), set()
        output = []

        def dfs(crs):
            if crs in done:
                return True
            if crs in curr:
                return False
            
            curr.add(crs)
            for pre in my_map[crs]:
                if not dfs(pre):
                    return False
            curr.remove(crs)
            done.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output