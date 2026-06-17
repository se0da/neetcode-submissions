class MinStack:
        
    def __init__(self):
        self.stk = []
        self.sec_stk = []


    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if self.sec_stk and self.sec_stk[-1] >= val:
            self.sec_stk.append(val)

        elif not self.sec_stk:
            self.sec_stk.append(val)


    def pop(self) -> None:
        if self.stk and self.sec_stk and self.stk[-1] == self.sec_stk[-1]:
            self.stk.pop()
            self.sec_stk.pop()
        
        elif self.stk and not self.sec_stk:
            self.stk.pop()

        else:
            self.stk.pop()

    def top(self) -> int:
        if self.stk: 
            return self.stk[-1]

    def getMin(self) -> int:
        if self.sec_stk: 
            return self.sec_stk[-1] 
        else: 
            return self.stk[-1]

