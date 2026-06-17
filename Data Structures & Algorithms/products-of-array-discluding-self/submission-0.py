class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        num = 1
        res = [1] * len(nums)
        for var in nums:
            num *= var
            pre.append(num)
        num = 1
        nums_rev = nums
        nums_rev.reverse()
        for var in nums_rev:
            num *= var
            post.insert(0,num)
        
        for i in range(len(nums)):
            if(i == 0):
                res[i] *= (post[1])
            elif(i == len(nums)-1):
                res[i] *= (pre[i-1])
            else:
                res[i] *= (pre[i-1]*post[i+1])

        return res
        



            

        