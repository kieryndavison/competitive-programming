class Solution:
    # Solution 1, most clear and nicely broken up into functions
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        
        # Finds the max number of points coming from the left
        def create_left(array):
            # We know that for i = 0, there are no points to the left so its value is just array[0]
            left = [array[0]] + [0] * (m - 1)
            
            # For i in 1 - m compute left[i] to be the max of left[i - 1] - 1 (subtract one since it is not the same col as i) and array[i]
            for i in range(1, m):
                left[i] = max(left[i-1] - 1, array[i])
            return left
        
        # Finds the max number of points coming from the right
        def create_right(array):
            # Similarly for i = m - 1, there are no points to the right so its value is just array[m - 1]
            right = [0] * (m - 1) + [array[-1]]

            # For i in 1 - m compute right[i] to be the max of right[i + 1] - 1 (subtract one since it is not the same col as i) and array[i]
            for i in range(m - 2, -1, -1):
                right[i] = max(right[i+1] - 1, array[i])
            return right
        
        # Keep track of the max points up to the previous row
        pre = points[0]
        for i in range(n - 1):
            # create the left, right and cur arrays
            left, right, cur = create_left(pre), create_right(pre), [0] * m
            
            # Go through each element in the current row and update the cur array to be the max of left[i], right[i], plus points[i+1][j]
            for j in range(m):
                cur[j] = points[i+1][j] + max(left[j], right[j])
            
            # copy the result of the current row to prev
            pre = cur[:]
        
        # Return the max of the points including the last row
        return max(pre)
    
    # Solution 2, slightly space optimized since we use the input array for the dp
    class Solution:
        def maxPoints(self, points: List[List[int]]) -> int:
            n = len(points)
            m = len(points[0])
            
            def create_left(array):
                left = [array[0]] + [0] * (m - 1)
                for i in range(1, m):
                    left[i] = max(left[i-1] - 1, array[i])
                return left
            
            def create_right(array):
                right = [0] * (m - 1) + [array[-1]]
                for i in range(m - 2, -1, -1):
                    right[i] = max(right[i+1] - 1, array[i])
                return right
            
            # Similar to the previous solution, but we don't need to keep track of the previous row  which 
            # reduces space complexity to O(1) and eliminates the need for copying which can be expensive
            for i in range(n - 1):
                left, right = create_left(points[i]), create_right(points[i])
                for j in range(m):
                    points[i+1][j] += max(left[j], right[j])
                
            return max(points[-1])

    # Solution 3, space optimized and time optimized (not time complexity but requires one less pass)
    class Solution:
        def maxPoints(self, points: List[List[int]]) -> int:
            n = len(points)
            m = len(points[0])
            
            # Instead of computing the left and right and then going through each element in the row again and updating 
            # it to be the max of the left and right plus points[i+1][j] we can just directly set the value of points[i+1][j] 
            # in the second pass, since we know points[i][j] is the max of the left and right
            for i in range(n - 1):
                for j in range(m - 2, -1, -1):
                    points[i][j] = max(points[i][j+1] - 1, points[i][j])
                for j in range(m):
                    if j != 0:
                        points[i][j] = max(points[i][j-1] - 1, points[i][j])
                    points[i+1][j] += points[i][j]
                
            return max(points[-1])
                