class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])

        # Optimization, if k large enough then we can just go straight down and then right to get to the goal
        if k >= m + n - 3:
            return m + n - 2
        
        queue = deque([(0, 0, 0, 0)])
        visited = set((0, 0, 0))        
        
        # BFS on row, col and the number of obstacles in the path, keeping track of the cells that we have already tried
        while queue:
            row, col, obstacles, length = queue.popleft()
            directs = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
            
            
            for new_row, new_col in directs:
                if 0 <= new_row < n and 0 <= new_col < m:
                    new_obstacles = obstacles + grid[new_row][new_col]
                    if (new_row, new_col, new_obstacles) not in visited and (grid[new_row][new_col] == 0 or obstacles < k):
                        
                        # Once we find a path since we are using BFS it will be a shortest path
                        if new_row + 1 >= n and new_col + 1 >= m:
                            return length + 1
                        
                        # Otherwise add the element to the queue and the visited set
                        queue.append((new_row, new_col, new_obstacles, length + 1))
                        visited.add((new_row, new_col, new_obstacles))
        
        return -1