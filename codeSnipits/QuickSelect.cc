int partition(vector<int>& nums, int l, int r) { 
    int x = nums[r], i = l; 
    for (int j = l; j <= r - 1; j++) { 
        if (nums[j] <= x) { 
            swap(nums[i], nums[j]); 
            i++; 
        } 
    } 
    swap(nums[i], nums[r]); 
    return i; 
} 

int kthSmallest(vector<int>& nums, int l, int r, int k) { 
    if (k > 0 && k <= r - l + 1) { 
        int index = partition(nums, l, r); 

        if (index - l == k - 1) 
            return nums[index]; 

        if (index - l > k - 1)  
            return kthSmallest(nums, l, index - 1, k); 

        return kthSmallest(nums, index + 1, r, k - index + l - 1); 
    } 
    return INT_MAX; 
} 