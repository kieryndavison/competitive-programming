# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        maxElements = []  
        row = [root] # Keep track of the current row of elements in the bst, starts with just the root      

        # While there are any elements in the current row
        while any(row):

            # Add the max element in the row to the result and update the row 
            # to contain the non-null elements in the next row of the tree
            curMax = row[0].val
            temp = [] 
            for node in row:
                curMax = max(curMax, node.val)
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            maxElements.append(curMax)
            row = temp
        
        return maxElements