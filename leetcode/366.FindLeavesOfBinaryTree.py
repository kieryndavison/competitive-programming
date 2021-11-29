# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        # Insert each node in the result at the index of the height of the node.
        def height(root):
            if root == None:
                return -1
            level = max(height(root.left), height(root.right)) + 1
            
            if level == len(res):
                res.append([root.val])
            else:
                res[level].append(root.val)
            
            return level
        
        height(root)
        return res