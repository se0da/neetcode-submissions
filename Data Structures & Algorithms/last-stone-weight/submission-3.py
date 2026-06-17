class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-v for v in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            v1 = -heapq.heappop(max_heap)
            v2 = -heapq.heappop(max_heap)

            if v1 > v2:
                heapq.heappush(max_heap, -(v1-v2))

            else:
                heapq.heappush(max_heap, -(v2-v1))
            
        return -max_heap[0]