# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]: 
        to_delete_set = set(to_delete)
        self.res = []
        self.find_nodes(root, to_delete_set, True)
        return self.res
    
    def find_nodes(self, root, to_delete, is_root):
        if root is None:
            return None
        
        # If the node is a root and is not in the delete set then we add it to the result
        root_deleted = root.val in to_delete
        if is_root and not root_deleted:
            self.res.append(root)

        # Recurse left and right, note that we know that if the current value was deleted then 
        # the left and right will be roots, hence why the is_root parameter can be set to root_deleted
        root.left = self.find_nodes(root.left, to_delete, root_deleted)
        root.right = self.find_nodes(root.right, to_delete, root_deleted)
        
        # If the node was deleted then we return None, otherwise we return the node
        return None if root_deleted else root
