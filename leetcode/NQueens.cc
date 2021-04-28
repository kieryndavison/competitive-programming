class Solution {
    bool isValid(vector<int> &flag, int r, int &n, int c) {
        return flag[c] && flag[n + r + c] && flag[4 * n - 2 + c - r];
    }

    void findAllArrangements(vector<vector<string>> &ans, vector<string> &curArrangement, vector<int> &flag, int r, int &n) {
        if (r == n) {
            ans.push_back(curArrangement);
            return;
        }

        for (int i = 0; i < n; ++i) {
            if (isValid(flag, r, n, i)) {
                flag[i] = flag[n + r + i] = flag[4 * n - 2 + i - r] = 0;
                curArrangement[r][i] = 'Q';
                findAllArrangements(ans, curArrangement, flag, r + 1, n);
                curArrangement[r][i] = '.';
                flag[i] = flag[n + r + i] = flag[4 * n - 2 + i - r] = 1;
            }
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<string> curArrangement(n, string(n, '.'));
        vector<int> flag(5 * n - 2, 1);
        findAllArrangements(ans, curArrangement, flag, 0, n);
        return ans; 
    }
};