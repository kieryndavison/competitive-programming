#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {

    //find longest subarray of array1 that is a subsequence of array2
    int longestSubarraySubsequence(vector<int>& array1, vector<int>& array2) {
        int n = array1.size();
        int maxLength = 0;
        vector<vector<int> > dp(n+1, vector<int>(n+1, 0));

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = array1[i-1] == array2[j-1] ? dp[i-1][j-1] + 1 : dp[i][j-1];
                maxLength = max(maxLength, dp[i][j]);
            }
        }

        return maxLength;
    }

public:
    int minOperations(vector<int>& array1, vector<int>& array2) {
        int lengthSubarraySubsequence = longestSubarraySubsequence(array1, array2);
        return array1.size() - lengthSubarraySubsequence;
    }
};

int main() {
    Solution sol;
    vector<int> array1{ 4,2,3,1,5,6 };
    vector<int> array2{ 3,1,4,6,5,2 };
    cout << sol.minOperations(array1, array2) << endl;

    vector<int> array3{ 3,2,4,7,1,5,6,8,10,9 };
    vector<int> array4{ 9,2,4,3,1,5,6,8,10,7 };
    cout << sol.minOperations(array3, array4) << endl;
}