class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        totalNum  = 0
        
        for i, pot in enumerate(flowerbed):
            # Check the left and right sides of the element if they exist and update the
            # value in the array to be 1 if we can place a flower there
            if pot == 0 and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0) and (i == 0 or flowerbed[i-1] == 0):
                totalNum += 1
                flowerbed[i] = 1
            
            # Slight optimiztation to return as soon as we can place at least n flowers in the array
            if totalNum >= n:
                return True
        
        return False