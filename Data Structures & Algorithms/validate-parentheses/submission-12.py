class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if my_map and stack and c in my_map:
                if my_map[c] != stack.pop():
                    return False
                
            else:
                stack.append(c)
        return True if len(stack) == 0 else False