class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.kthSmallest(points, k, 0, len(points) - 1)

        # after kthsmallest we know that the k points with shortest distance 
        # to the origin will be in the array in indexes 0...k
        return points[:k]

    # Organize the array to have all elements <= kth element in the left 
    # half and elements > k in the right half
    def kthSmallest(self, points, k, l, r):
        # if we are out of bounds return 
        if l >= len(points) or r < 0: return 

        # partition the array
        index = self.partition(points, l, r)

        # if we index of the partition is equal to k then we know that the k points 
        # with with the shortest distances to the orgiin are in the array[:k] so we return 
        if index == k: return 

        # if index > k then we have too many points and we look in the left half of the array
        elif index > k: return self.kthSmallest(points, k, l, index - 1)
        
        # otherwise index < k so we have not enough many points and we look in the right half of the array
        else: self.kthSmallest(points, k, index + 1, r)

    def partition(self, points, l, r):
        # set the pivot to be the last element in the segement of the array we are looking at
        pivotDist = points[r][0] ** 2 + points[r][1] ** 2
        # set the starting pivot index to be the first index in the segement
        i = l

        # go through the segement, swap element at i with elment at j if the element 
        # at j is less than or equal to the pivot, and increment i
        for j in range(l, r):
            if (points[j][0] ** 2 + points[j][1] ** 2) <= pivotDist:
                points[j], points[i] = points[i], points[j]
                i += 1
        
        # put the pivot in the correct place and return the pivot index
        points[r], points[i] = points[i], points[r]
        return i
