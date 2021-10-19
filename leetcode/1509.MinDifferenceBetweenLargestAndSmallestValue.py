class Solution:
    # consider the 4 options: removing first 3, removing last 3, 
    # removing first 1 and last 2 and removing first 2 and last 1
    
    # quick sort version
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        nums.sort()
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))
    
    # quick select version
    def minDifference(self, nums: List[int]) -> int:        
        largest4Values = heapq.nlargest(4, nums)[::-1]
        smallest4Values = heapq.nsmallest(4, nums)
        
        return min(a - b for a, b in zip(largest4Values, smallest4Values))
