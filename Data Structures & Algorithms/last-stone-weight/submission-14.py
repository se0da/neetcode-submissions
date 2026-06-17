class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-v for v in stones]
        heapq.heapify(hp)
        while len(hp) > 1:
            v1 = -(heapq.heappop(hp))
            v2 = -(heapq.heappop(hp))
            if v1 > v2:
                heapq.heappush(hp,-(v1-v2))
            elif v2 < v1:
                heapq.heappush(hp,-(v2-v1))
            
        return -(hp[0]) if hp else 0

        