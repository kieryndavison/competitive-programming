#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 0) {
            return 0;
        }

        grid[r][c] = 0;
        return (1 + dfs(grid, r+1, c) + dfs(grid, r-1, c) + dfs(grid, r, c+1) + dfs(grid, r, c-1));
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.size() < 1) {
            return 0;
        }
        
        int maxSize = 0;
        for (int i = 0; row = grid.size(); i < row; i++) {
            for (int j = 0; col = grid[0].size(); j < col; j++) {
                maxSize = max(maxSize, dfs(grid, i, j));
            }
        }

        return maxSize;
    }
};

// Example:
// [[0,0,1,0,0,0,0,1,0,0,0,0,0],
//  [0,0,0,0,0,0,0,1,1,1,0,0,0],
//  [0,1,1,0,1,0,0,0,0,0,0,0,0],
//  [0,1,0,0,1,1,0,0,1,0,1,0,0],
//  [0,1,0,0,1,1,0,0,1,1,1,0,0],
//  [0,0,0,0,0,0,0,0,0,0,1,0,0],
//  [0,0,0,0,0,0,0,1,1,1,0,0,0],
//  [0,0,0,0,0,0,0,1,1,0,0,0,0]]