class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(list)

        for num in nums:
            ans[num].append(num)

        # Sorting the dictionary keys based on the length of their corresponding lists
        sortlist = sorted(ans.items(), key=lambda x: len(x[1]))

        answer = sortlist[-k:len(sortlist)]
        keys = [item[0] for item in answer]
        return keys
            