# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs (self, root: TreeNode, count) :
        if not root: return 0
        
        # bitshift 1 by root.val - 1 and XOR it with the current count
        # keeps track of whether we have seen root.val an even or odd number of times
        count ^= 1 << (root.val - 1)
        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        
        if root.left == root.right:

            # In order for a given path to be Pseudo-Palindromic we must have at most 
            # one value that occurs an odd number of times. One way we can check this 
            # is by checking if only one bit in count is 1. In otherwords count must 
            # be equal to a power of 2^n. In binary we know that 2^n - 1 will have no
            # values in common with 2^n, therefore if we add them together the result 
            # should be 0
            if count & (count - 1) == 0:
                res += 1
        return res
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.dfs(root, 0)