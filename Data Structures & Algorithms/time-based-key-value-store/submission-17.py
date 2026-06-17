class TimeMap:

    def __init__(self):
        self.my_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        items = self.my_map.get(key)
        if not items:
            return ""

        l, r = 0, len(items)-1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            if items[m][1] <= timestamp:
                res = items[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        

