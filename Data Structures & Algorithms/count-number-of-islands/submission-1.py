class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or (r, c) in visit 
                or r == rows or c == cols or grid[r][c] == '0'):
                return 

            
            visit.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    self.count += 1
 
        return self.count

                    



        