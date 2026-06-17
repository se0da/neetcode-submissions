class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            print(stk)
            while stk and stk[-1][1] < t:
                stk_i, stk_t = stk.pop()
                print(stk_i)
                print(stk_t)
                output[stk_i] = i - stk_i
            stk.append([i,t])
        
        return output

