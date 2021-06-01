# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Classic pre-order traversal but keeping track of the current level
    def dfs(self, node, res, level):
        if node is None: return

        # If we found the first element in the level then add it to the result
        if level == len(res): res.append(node.val)

        # Otherwise update the result at the current level to be the max of 
        # its value and the value of the current node
        else: res[level] = max(res[level], node.val)

        # Recurse on the left and right nodes with level + 1
        self.dfs(node.left, res, level + 1)
        self.dfs(node.right, res, level + 1)


    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res, 0)
        return res