class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"{": "}", "[": "]", "(": ")"}
        for c in s:
            if c in dict:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()

                if dict[popped] != c:
                    return False
        return not stack
