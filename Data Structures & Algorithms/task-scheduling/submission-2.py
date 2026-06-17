class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-v for v in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1 

            if max_heap:
                val = 1 + heapq.heappop(max_heap)
                if val:
                    q.append((val, time + n))
                
            if q and q[0][1] == time:
                var = q.popleft()
                heapq.heappush(max_heap, var[0])
            
        return time 

