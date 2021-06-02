class Solution:

    # Compute the prefix sum for each element in the array and store it in a list
    def __init__(self, w: List[int]):
        self.prefixSum = []
        curSum = 0
        for num in w:
            curSum+= num
            self.prefixSum.append(curSum)

    # Binary search for the random number between 1 and the total sum generated 
    def pickIndex(self) -> int:
        low, high = 0, len(self.prefixSum)
        rand = random.randint(1, self.prefixSum[-1])
        
        while low < high:
            mid = low + (high - low) // 2
            if self.prefixSum[mid] >= rand: high = mid
            else: low = mid + 1
        
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()