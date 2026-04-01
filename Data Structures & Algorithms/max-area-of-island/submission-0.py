class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        self.area = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols 
                or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            count = 1

            count += dfs(r - 1, c)
            count += dfs(r + 1, c)
            count += dfs(r, c - 1)
            count += dfs(r, c + 1)
            return count
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    curr = dfs(r, c)
                    self.area = max(self.area, curr)
        return self.area
        

        