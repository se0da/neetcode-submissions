class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_stk = []

        for token in tokens:
            print(token)
            print(int_stk)
            if token == "+":
                int_stk.append(int(int_stk.pop())+int(int_stk.pop()))

            elif token == "-":
                first = int(int_stk.pop())
                second = int(int_stk.pop())
                int_stk.append(second-first)

            elif token == "*":
                int_stk.append(int(int_stk.pop())*int(int_stk.pop()))

            elif token == "/":
                first = int(int_stk.pop())
                second = int(int_stk.pop())
                int_stk.append(int(second/first))
            else:
                int_stk.append(token)    
            
        return int(int_stk[-1])
