class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-v for v in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)
            if val1 < val2:
                heapq.heappush(max_heap, -(val2-val1))
            elif val2 < val1:
                heapq.heappush(max_heap, -(val1-val2))
        return -max_heap[0] if len(max_heap) > 0 else 0

