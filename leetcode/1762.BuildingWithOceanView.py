class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curMax = -1 
        res = []
        
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > curMax:
                res.append(i)
                curMax = heights[i]
            
        return res[::-1]