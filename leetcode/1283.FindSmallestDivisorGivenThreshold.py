class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        low, high = 1, max(nums)

        # binary search for the divisor 
        while low <= high:
            mid = (low + high) // 2
            
            # if sum is greater than the threshold then we try a larger divisor
            if self.calculateSumForDivisor(nums, mid) > threshold:
                low = mid + 1
            
            # otherwise then we try a smaller divisor
            else: 
                high = mid - 1
        
        return low
    
    # calculate the sum of the array for the given divisor
    def calculateSumForDivisor(self, nums, divisor):
        sumElements = 0
        
        for num in nums:
            sumElements += (num + divisor - 1) // divisor
        
        return sumElements