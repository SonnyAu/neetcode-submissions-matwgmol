class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(grid, r, c, visit):
            if (min(r, c) < 0 or (r, c) in visit 
                or r == rows or c == cols or grid[r][c] == '0'):
                return 

            
            visit.add((r, c))

            dfs(grid, r - 1, c, visit)
            dfs(grid, r + 1, c, visit)
            dfs(grid, r, c - 1, visit)
            dfs(grid, r, c + 1, visit)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    self.count += 1
                dfs(grid, r, c, visit)
 
        return self.count

                    



        