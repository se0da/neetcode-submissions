class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in ('*', '/', '+', '-'):
                first, second = int(stack.pop()), int(stack.pop())
                if c == '*':
                    stack.append(first * second)
                if c == '/':
                    stack.append(int(float(second) / first))
                if c == '-':
                    stack.append(second - first)
                if c == '+':
                    stack.append(first + second)
            else:
                stack.append(c)
            
        return int(stack[0])