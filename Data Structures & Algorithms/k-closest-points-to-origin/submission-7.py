class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x, y in points:
            distance = x**2 + y**2
            hp.append([distance,x,y])

        res = []
        heapq.heapify(hp)
        while k:
            dist, x, y = heapq.heappop(hp)
            res.append((x,y))
            k -= 1
        
        return res