class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]
        def memoization(r, c):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if cache[r][c] != -1:
                return cache[r][c]
            cache[r][c] = memoization(r, c + 1) + memoization(r + 1, c)
            return cache[r][c]
        return memoization(0, 0)

        