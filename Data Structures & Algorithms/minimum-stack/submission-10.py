class MinStack:
    def __init__(self):
        self.stack1 = []  # Main stack
        self.stack2 = []  # Min stack

    def push(self, val: int) -> None:
        self.stack1.append(val)
        # Push to min stack if it's empty or val is <= current min
        if not self.stack2 or val <= self.stack2[-1]:
            self.stack2.append(val)

    def pop(self) -> None:
        # Pop from both stacks if the top of stack1 equals the top of stack2
        if self.stack1:
            popped = self.stack1.pop()
            if popped == self.stack2[-1]:
                self.stack2.pop()

    def top(self) -> int:
        # Return the top of the main stack
        return self.stack1[-1] if self.stack1 else None

    def getMin(self) -> int:
        # Return the top of the min stack
        return self.stack2[-1] if self.stack2 else None
