class Solution:
    # Version 1 
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = defaultdict(lambda: -1)
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            res.append(nextGreater[num])
            
        return res
    
    # Version 2 more pythonic 
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = defaultdict(lambda: -1)
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)
            
        return [nextGreater[num] for num in nums1]