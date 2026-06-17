class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p,s))
        
        cars.sort(reverse = True)

        eta_stk = []

        for p, s in cars:
            eta = (target - p) / s
            if not eta_stk:
                eta_stk.append(eta)
            elif eta > eta_stk[-1]:
                eta_stk.append(eta)
            
        return len(eta_stk)
