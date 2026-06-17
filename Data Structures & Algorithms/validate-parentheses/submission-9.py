class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {')' : '(', '}' : '{', ']' : '['}

        stack = []

        for c in s:
            if c in my_map and stack:
                popped = stack.pop()
                if my_map[c] != popped:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False