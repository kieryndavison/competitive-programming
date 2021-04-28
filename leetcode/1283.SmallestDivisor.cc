class Solution {
public:
    int calculateSum(vector<int>& nums, int x) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += (nums[i] / x) + (nums[i] % x == 0 ? 0 : 1); 
        }
        return sum;
    }
    
    int binarySearch(vector<int>& nums, int low, int high, int x) { 
        while (low <= high) { 
            int mid = low + ((high - low) / 2); 

            int sum = calculateSum(nums, mid);
                
            if (sum > x) low = mid + 1; 
            else high = mid - 1; 
        } 
        return low; 
    } 

    int smallestDivisor(vector<int>& nums, int threshold) {
        int maxNum = *max_element(begin(nums), end(nums));
                        
        return binarySearch(nums, 1, maxNum, threshold);
    }
};