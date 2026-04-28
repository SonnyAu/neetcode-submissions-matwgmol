class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numS = ''
        for n in digits:
            numS += str(n)
        ans = 1 + int(numS)
        return list(map(int, str(ans)))

        