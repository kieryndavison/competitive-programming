#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end()); 
    vector<vector<int>> result;
    
    if (nums.size() < 3) return result;
    
    for (int i = 0; i < nums.size() - 2;) {
        int j = i + 1;
        int k = nums.size() - 1;
        
        if (nums[i] > 0) break;
        
        while (j < k) {
            int sum = nums[i] + nums[j] + nums[k];
            if (sum < 0) j++;
            else if (sum > 0) k--;
            else {
                vector<int> triple = {nums[i], nums[j], nums[k]};
                result.emplace_back(triple);
                j++;
                k--;
                while( j < k && nums[j] == nums[j-1] )
                    j++;
                while( j < k && nums[k] == nums[k+1] )
                    k--;
            } 
        }
        i++;
        while( i > 0 && i < nums.size() - 2 && nums[i] == nums[i-1] )
            i++;
    }
    return result;
}

int main () {
    vector<int> nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> solution = threeSum(nums);
    for (int i = 0; i < solution.size(); i++) {
        for (int j = 0; j < solution[0].size(); j++) {
            cout << solution[i][j];
            if (j != (solution[0].size() - 1)) cout << ",";
        }
        cout << endl;
    }
}