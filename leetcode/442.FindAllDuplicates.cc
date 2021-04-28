class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> dups;
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]);
            if (nums[index - 1] < 0) dups.emplace_back(index);
            else nums[index - 1] = -nums[index - 1];
        }
        return dups;
    }
};