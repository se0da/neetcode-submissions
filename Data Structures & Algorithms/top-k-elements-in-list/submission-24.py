class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(list)
        for num in nums:
            myMap[num] = myMap.get(num,0) + 1
        
        arr = []
        
        for num, cnt in myMap.items():
            arr.append([cnt,num])
        
        arr.sort(reverse = True)
        ans = []

        for i in range(k):
            ans.append(arr[i][1])

        return ans

        
            