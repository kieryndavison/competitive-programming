class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        runningProd = 1
        res = [1] * len(nums)
        
        # Compute the product of all elements that occur before the current element
        for i in range(0, len(nums)):
            res[i] *= runningProd
            runningProd *= nums[i]
        
        runningProd = 1

        # Compute the product of all elements that occur after the current element
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= runningProd
            runningProd *= nums[i]
        
        return res