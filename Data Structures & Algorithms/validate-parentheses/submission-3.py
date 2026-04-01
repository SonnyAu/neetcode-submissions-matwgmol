class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in bracket_map:
                if len(stack) > 0 and bracket_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False
        