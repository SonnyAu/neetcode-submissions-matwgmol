class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {']': '[', '}': '{', ')': '('}
        stack = []

        for c in s:
            if c in pairs:
                if not stack:
                    return False
                curr = stack.pop()
                if pairs[c] == curr:
                    continue
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        