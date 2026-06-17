class Solution:
    def isValid(self, s: str) -> bool:
        my_map = { ")" : "(","}" : "{","]" : "["}
        stack = []
    
        for c in s:
            if stack and c in my_map:
                if stack.pop() != my_map[c]:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False























