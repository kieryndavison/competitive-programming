class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        // use dp only need to keep track of the current column
        int dp[cols];

        int maxSquare = 0, prev = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int temp = dp[j];
                if (i == 0 || j == 0 || matrix[i][j] == '0') {
                    dp[j] = matrix[i][j] - '0';
                } else {
                    // this is equivalent to dp[j] = min({dp[i][j-1], dp[i-1][j-1], dp[i-1][j]}) + 1;
                    dp[j] = min({dp[j-1], prev, dp[j]}) + 1;
                }

                // keep track of the max length for the square and dp[i-1][j-1]
                maxSquare = max(maxSquare, dp[j]);
                prev = temp;
            }
        }

        // calculate the square size from its length
        return maxSquare * maxSquare;
    }
};