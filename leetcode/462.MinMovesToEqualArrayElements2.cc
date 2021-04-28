class Solution {
public:
    int minMoves2(vector<int>& nums) {
        nth_element(nums.begin(), nums.begin() + nums.size() / 2, nums.end());
        int median = nums[nums.size() / 2], total = 0;
        for (int i = 0; i < nums.size(); i++) {
            total += abs(nums[i] - median);
        }
        return total;
    }
};
