class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(list)

        for var in nums:
            ans[var].append(var)

        sortedList = sorted(ans.items(), key=lambda x: len(x[1]), reverse=True)
        return[items[0] for items in sortedList[0:k]]
    

