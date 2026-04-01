from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1,1), (-1, -1), (1, -1), (-1, 1)]
        while q:
            r, c, length = q.popleft()
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr >= N or nc >= N 
                    or (nr, nc) in visit or grid[nr][nc] == 1):
                    continue
                q.append((nr, nc, length + 1))
                visit.add((nr, nc))
        return -1

        