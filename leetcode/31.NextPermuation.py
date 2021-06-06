class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 1, len(nums) - 1
        
        # Find first number that is smaller than the one before it
        while i >= 1 and nums[i] <= nums[i-1]:
            i -= 1
        
        # Number is already its largest permuation
        if i == 0:
            nums.reverse()
            return

        # Find smallest number after the number at i-1 that is larger than it
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        
        # swap the number at i - 1 with the smallest larger number
        nums[j], nums[k] = nums[k], nums[j]

        # reverse all the elements after the value we swapped 
        l, r = k+1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1