class SparseVector:

    # Store all the non zero elements and their index in a list
    def __init__(self, nums: List[int]):
        self.nonZero = []
        for i, num in enumerate(nums):
            if num != 0: self.nonZero.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        index1, index2 = 0, 0
        
        # go through all the non zero elements in the arrays
        while index1 < len(self.nonZero) and index2 < len(vec.nonZero):
            
            # if the indexes of the elements match up then multiply the values, 
            # add it to the product and increment both indexes 
            if self.nonZero[index1][0] == vec.nonZero[index2][0]:
                prod += self.nonZero[index1][1] * vec.nonZero[index2][1]
                index1 += 1
                index2 += 1
            
            # otherwise increment the index for list of non-zero elements that 
            # corresponds to the smaller nonZero index
            elif self.nonZero[index1][0] < vec.nonZero[index2][0]:
                index1 += 1
            else: index2 += 1
                
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)