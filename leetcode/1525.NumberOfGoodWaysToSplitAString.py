class Solution:
    def numSplits(self, s: str) -> int:
        leftCount = collections.Counter()
        rightCount = collections.Counter(s)
        res = 0
        
        for char in s:
            leftCount[char] += 1
            rightCount[char] -= 1
            
            if rightCount[char] == 0:
                del rightCount[char]
                
            if len(leftCount) == len(rightCount):
                res += 1
        
        return res