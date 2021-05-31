# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        i, j = 0, cols - 1
        
        # loop while i and j are in range
        while i < rows and j >= 0:

            # if we find a 1 go left 
            if binaryMatrix.get(i, j): j -= 1

            # if we find a 0 go down
            else: i += 1
        
        # j contains the rightmost column with all 0s, so add 1 to it to get the leftmost column 
        # with at least one 1, if j is equal to the last index in the array then there are no 1s 
        # so return -1
        return j + 1 if j < cols - 1 else -1