class Solution {

public:
    string kthSmallestPath(vector<int>& destination, int k) {
        int r = destination[0];
        int c = destination[1];

        int total = r + c;

        // Find pascals triangle for the coordinates specified
        int dp[r+1][c+1];
        dp[0][0] = 1;
        
        for (int i = 0; i <= r; i++) {
            for (int j = 0; j <= c; j++) {
                dp[i][j] = 1;
            }
        }

        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }

        // Determine the kth smallest path from pascales triangle
        string res = "";
        while (r > 0 and c > 0) {
            if (dp[r][c-1] >= k) {
                res += "H";
                c -= 1;
            } else {
                res += "V";
                k -= dp[r][c-1];
                r -= 1;
            }
        }
    
        while (r > 0) {
            res += "V";
            r -= 1;
        }
    
        while (c > 0) {
            res += "H";
            c -= 1;
        }

        return res;
    }
};