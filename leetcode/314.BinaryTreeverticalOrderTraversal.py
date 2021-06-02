# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # Edge case handling
        if root is None: return []
        
        # Define dictionary to hold node values for each column
        dictionary = defaultdict(list)

        # Define variables to hold the minimum and maximum column value so that 
        # we can go through the dictionary at the end without sorting it
        minCol, maxCol = 0, 0

        # Define a queue for the BFS and add the first element and its column value (0)
        queue = deque([(root, 0)])
        
        # iterate while there are elements in the queue
        while queue:
            node, col = queue.popleft()

            # Update the max and min column values based on the current column value
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            
            # Add the value of the node to list for its column
            dictionary[col].append(node.val)
            
            # If we can go left add the left node and column value - 1 to the queue 
            if node.left: queue.append((node.left, col-1))
            
            # If we can go right add the right node and column value + 1 to the queue 
            if node.right: queue.append((node.right, col+1))
        
        # Return the lists in the dictionary in left to right order by going through the column values from min to max
        return [dictionary[x] for x in range(minCol, maxCol + 1)]