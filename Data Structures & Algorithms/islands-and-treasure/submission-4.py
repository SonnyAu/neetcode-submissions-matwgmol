class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        q = deque()
        directions = [[0,1], [1,0], [-1,0],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
        