class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {')':'(', '}':'{', ']':'['}
        stk = []

        for c in s:
            if c not in my_map.keys():
                stk.append(c)
            
            elif stk and stk[-1] == my_map[c]:
                stk.pop()

            else:
                return False

            print(stk)

        return False if len(stk) > 0 else True