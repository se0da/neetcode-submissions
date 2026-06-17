class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-v for v in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                if val:
                    q.append([val,n+time])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time

