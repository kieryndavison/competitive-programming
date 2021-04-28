#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    map<int, int> values;
    
    //find values that map to the target
    for (int i = 0; i < nums.size(); i++) {
        int val = target - nums[i];
        if (values.find(val) != values.end() && values.find(val)->second != i) {
            return vector<int>{i, values.find(val)->second};
        }
        values.insert(make_pair(nums[i], i));
    }
    return vector<int>{};
}

int main () {
    vector<int> nums = {3,3};
    vector<int> solution = twoSum(nums, 6);
    for (int i = 0; i < solution.size(); i++) {
        cout << solution[i];
        if (i == 0) cout << ",";
        else cout << endl;
    }
}