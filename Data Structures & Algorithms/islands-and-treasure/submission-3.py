class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        '''
        setup:
        find all the treasure chests for first pass to add to queue 
        second pass, use bfs to traverse all directions
        as we traverse, update curr cell to use previous traversed cell + 1 [0 -> 1 -> 2]
        '''

        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        # q = [(0, 3), (1, 2), (0, 1)]
        # curr = (3, 0) => 
        '''
        [3,-1,0, 1],
        [2,2,1,-1],
        [1,-1,2,-1],
        [0,-1,3,4]
        '''
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= rows or nc >= cols or min(nr, nc) < 0 or grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = 1 + grid[r][c] # update curr cell w/ previous cell's dist
                q.append((nr, nc))


                
        