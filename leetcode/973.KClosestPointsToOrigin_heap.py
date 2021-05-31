class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        # Go through the array of points and add the negative of the distance to 
        # the origin to the heap, if the heap size is greater than k then we pop 
        # the smallest element from the heap = largest distance to the origin since 
        # we insert the negative of the distance
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-distance, point))
            if (len(heap) > k):
                heapq.heappop(heap)
        
        # return all the points in the heap at then end
        return [tuple[1] for tuple in heap]