# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        cur = root

        while cur != None:
            if abs(target - cur.val) < abs(target - res):
                res = cur.val

            cur = cur.left if cur.val > target else cur.right

        return res