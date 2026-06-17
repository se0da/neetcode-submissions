class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        # Push value to main stack
        self.stack.append(val)
        # Push to min_stack if it is the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # If the top of both stacks matches, pop from both
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        # Return the top element of the stack, or None if empty
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top of min_stack if it exists, or None
        return self.min_stack[-1] if self.min_stack else None
