class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum, res = 0, 0
        dictionary = {0: 1}
        
        # Based on the idea that sum(i,j) = sum(0, j) - sum(0, i - 1), to compute this we have a dictionary 
        # which contains all the pre-sums aka sum(0, i - 1). Each time we go through the loop if sum(0, j) 
        # aka curSum - sum(i,j) aka k, is in the presum dictionary then we add the frequency of sum(0, i-1) 
        # to the res. We have to add to the frequency since we can have negative numbers which means that we 
        # can have the same number twice 
        for num in nums:
            curSum += num
            if curSum - k in dictionary:
                res += dictionary[curSum - k]
            
            dictionary[curSum] = dictionary[curSum] + 1 if curSum in dictionary else 1

        return res