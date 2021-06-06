class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numIslands += 1
                    self.dfs(grid, j, i)
        
        return numIslands

    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] != '1':
            return
        
        grid[y][x] = '#'
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x, y - 1)
