class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(list)

        for var in nums:
            ans[var].append(var)
        
        sortedNums = sorted(ans.items(), key=lambda x: len(x[1]), reverse = True)
        return [item[0] for item in sortedNums[0:k]]
     


            