class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)
            if val1 == val2:
                continue
            if val1 < val2:
                heapq.heappush(max_heap, -(val2-val1))
            elif val1 > val2:
                heapq.heappush(max_heap, -(val1-val2))
            
        return -max_heap[0] if max_heap else 0