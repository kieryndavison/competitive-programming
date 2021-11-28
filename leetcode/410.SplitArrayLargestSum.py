class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # we know that the sum of the largest subarray must be between the largest value 
        # in the array and the sum of the array so binary search between these values
        min_val = max(nums)
        max_val = sum(nums)
                
        while min_val < max_val:
            mid = (min_val + max_val) // 2
            # if the array can be split into <= m subarrays with sums <= mid, then the sum of the largest subarray must be <= mid            
            if self.check_num_subarrays(mid, nums) <= m:
                max_val = mid
            # otherwise the sum of the largest subarray must be > mid            
            else:
                min_val = mid + 1
            
        
        return min_val
    
    # Check the number of arrays that the array would be split into with sums <= mid
    def check_num_subarrays(self, sum_subarray, nums):
        num_subarrays = 0
        cur_sum = 0
        
        for num in nums:
            if cur_sum + num > sum_subarray:
                cur_sum = 0
                num_subarrays += 1
            cur_sum += num
        
        return num_subarrays + 1
