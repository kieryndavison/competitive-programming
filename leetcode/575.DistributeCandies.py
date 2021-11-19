class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        numCanEat = len(candyType) // 2
        numCandyTypes = len(set(candyType))
        
        return min(numCanEat, numCandyTypes)