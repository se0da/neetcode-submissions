class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        hp = [-v for v in count.values()]
        heapq.heapify(hp)
        time = 0

        while hp or q:
            time += 1
            if hp:
                v = 1 + heapq.heappop(hp)
                if v:
                    q.append((v,n+time))
            if q and q[0][1] == time:
                v, t = q.popleft()
                heapq.heappush(hp, v)
            
        return time
