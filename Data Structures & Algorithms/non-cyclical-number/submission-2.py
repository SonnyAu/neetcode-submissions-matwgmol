class Solution:
    def isHappy(self, n: int) -> bool:

        def sumSquare(n):
            curr = 0
            for c in str(n):
                curr += pow(int(c), 2)
            return curr
        seen = set()
        while n:
            n = sumSquare(n)
            if n == 1:
                return True
            elif n in seen:
                break
            seen.add(n)
        return False

        