class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = [-v for v in nums]
        heapq.heapify(hp)
        while True:
            k -= 1
            if k == 0:
                return -(hp[0])
            heapq.heappop(hp)
        
            