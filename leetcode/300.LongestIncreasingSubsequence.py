class Solution:
    # slight memory conservation
    def lengthOfLIS(self, nums: List[int]) -> int:
        minCharAtLength = [0] * len(nums)
        size = 0
        
        for num in nums:
            index = self.binarysearch(num, minCharAtLength, 0, size)
            minCharAtLength[index] = num
            size = max(size, index + 1)
        
        return size
    
    def binarysearch(self, num, array, l, r):
        while (l < r):
            mid = (l + r) // 2
            
            if array[mid] < num:
                l = mid + 1
            else: 
                r = mid
        
        return l
    
    # original solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        minCharAtLength = []
        
        for num in nums:
            index = self.binarysearch(num, minCharAtLength)
            if index >= len(minCharAtLength):
                minCharAtLength.append(num)
            else:
                minCharAtLength[index] = num
        
        return len(minCharAtLength)
    
    def binarysearch(self, num, array):
        l = 0
        r = len(array)
        
        while (l < r):
            mid = (l + r) // 2
            
            if array[mid] < num:
                l = mid + 1
            else: 
                r = mid
        
        return l