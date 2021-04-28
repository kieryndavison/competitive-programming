class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output(nums.size(), 1);
        int runningProd = 1;
        for (int i = 0; i < nums.size(); i++) {
            output[i] *= runningProd;
            runningProd *= nums[i];
        }

        runningProd = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            output[i] *= runningProd;
            runningProd *= nums[i];
        }

        return output;
    }
};