class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ("+","-","/","*"):
                first = int(stack.pop())
                second = int(stack.pop())
                if c == "*":
                    stack.append(first*second)
                elif c == "/":
                    stack.append(int(float(second)/first))
                elif c == "-":
                    stack.append(second-first)
                else:
                    stack.append(first+second)
            else:
                stack.append(c)
        return int(stack[0])