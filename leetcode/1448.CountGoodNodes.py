# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(cur, maxVal):
            if not cur: return 0
            maxVal = max(maxVal, cur.val)
            return dfs(cur.left, maxVal) + dfs(cur.right, maxVal) + (cur.val >= maxVal)
        
        return dfs(root, float('-inf'))