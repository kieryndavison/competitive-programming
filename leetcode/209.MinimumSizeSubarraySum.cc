class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {        
        int start = 0, ans = INT_MAX, subSum = 0;

        for (int i = 0; i < nums.size(); i++) {
            subSum += nums[i];
            while (subSum >= s) {
                ans = min(ans, i + 1 - start);
                subSum -= nums[start++];
            }
        }
        
        return (ans != INT_MAX) ? ans : 0;
    }
};