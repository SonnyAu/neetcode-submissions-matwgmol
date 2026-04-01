class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {"{": "}", "[": "]", "(":")"}

        stack = []

        for i, c in enumerate(s):
            if c in brackets:
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if brackets[top] != c:
                        return False
                else:
                    return False

        return not stack
                
