class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(list)

        for num in nums:
            ans[num].append(num)

        sortedList = sorted(ans.items(), key=lambda x : len(x[1]))
        sortedList = sortedList[-k:len(nums)]
        keys =  [items[0] for items in sortedList]
        return keys

            