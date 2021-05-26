# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        self.boundary = [root.val]
        
        def findBoundary(curNode, left, right):
            if curNode is None: return

            # Left boundary case
            if left: self.boundary.append(curNode.val)
                
            # Leaf node case 
            if not left and not right and curNode.left is None and curNode.right is None:
                self.boundary.append(curNode.val)
            
            # Go left, keep right true if the node does not have a right element
            findBoundary(curNode.left, left, right and not curNode.right)
            
            # Go right, keep left true if the node does not have a left element
            findBoundary(curNode.right, left and not curNode.left, right)
            
            # Right boundary case 
            if right: self.boundary.append(curNode.val)
            
        # Perform the dfs on both the left and right subtrees
        findBoundary(root.left, True, False)
        findBoundary(root.right, False, True)
        
        return self.boundary