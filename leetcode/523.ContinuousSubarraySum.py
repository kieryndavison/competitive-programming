class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Keep track of the prefix sum of the numbers, the prefixSums seen so far and their index
        prefixSum = 0
        seen = {0: -1}
        
        for i, num in enumerate(nums):

            # For each element in the array add its value to the prefix array 
            prefixSum += num

            # mod the prefix sum by k to keep the value of prefix sum between 0 and k
            if k != 0: prefixSum %= k

            # we have seen the prefix sum value before at an index > 1 before the current 
            # index then we return true
            if prefixSum in seen:
                if i > seen[prefixSum] + 1: return True

            # otherwise add the prefixSum to the dictionary with its index value
            else: seen[prefixSum] = i
        
        return False
             