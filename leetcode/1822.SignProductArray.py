class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # optimization for the case where there is a 0 in the array 
        # (since anything times 0 is still 0 the product will the 0)
        if 0 in nums: return 0
        
        # Keep track of the sign of the product
        sign = 1
        
        # Update the sign if we see a negative
        for num in nums:
            if num < 0: sign = -sign
        
        return sign