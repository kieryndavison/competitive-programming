class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2, minDist = -1, -1, len(wordsDict)

        # Keep track of the most recent index of each word in the list 
        # and update the minimum distance if both words have been seen 
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                minDist = min(minDist, abs(i1 - i2))
        
        return minDist
