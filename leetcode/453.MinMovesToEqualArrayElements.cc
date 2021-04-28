#define MIN(a,b) a<b? a: b

class Solution {
public:
    int minMoves(vector<int>& nums) {
        long long int sum = 0, minVal = INT_MAX;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            minVal = MIN(minVal, nums[i]);
        }
        return sum - (nums.size() * minVal);
    }
};