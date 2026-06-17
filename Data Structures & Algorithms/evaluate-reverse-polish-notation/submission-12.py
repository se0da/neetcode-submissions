class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ("+","-","/","*")
        for c in tokens:
            if c in operand:
                first, second = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(first + second)
                elif c == "-":
                    stack.append(second-first)
                elif c == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(float(second) / first))
            else:
                stack.append(int(c))
        
        return stack[0]
        