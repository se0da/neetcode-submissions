class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap that keeps track of number of occurences for each number
        freq = [[] for i in range(len(nums) + 1)] #bucket, the size of the amount of   
        #arrays in the bucket is limited to the size of the input array + 1 because
        #it will be 0 - 6 and a number can appear 6 times if the size of nums is 5

        for n in nums: # this going through the nums array and making the key value
        # the number and the value number the number of times it comes up
            count[n] = count.get(n,0)+1
        
        #this separates n into the key and c into the value
        #we are going through count.items in order to view the values
        #freq[c].append(n) is taking the count values of the hashmap and using it to 
        #guide the freq array. basically the freq array number will hold the number for 
        #the number 
        for n, c in count.items():
            freq[c].append(n)
        
        #array for the result
        res = []

        #this is going backwards starting from the freq array and going back one 
        for i in range(len(freq)-1, 0, -1):
            #go thru the freq array if there are more than one
            for n in freq[i]:
                #add it to the answer
                res.append(n)
                #if the answer has k values return res
                if len(res) == k:
                    return res
                
