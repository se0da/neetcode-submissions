class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = [-v for v in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            one = (heapq.heappop(heap))
            two = (heapq.heappop(heap))
            if one > two:
                heapq.heappush(heap,-(one-two))
            elif two > one:
                heapq.heappush(heap,-(two-one))
            
        return -(heapq.heappop(heap)) if heap else 0