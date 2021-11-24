class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        extra = 0
        x1, y1 = location
        
        # Compute the angle in radians for each point and save any values 
        # that are the same as the location so they can be added to the total
        for x2, y2 in points:
            if x1 == x2 and y1 == y2:
                extra += 1
            else:
                point_angle = math.atan2(y2 - y1, x2 - x1)
                angles.append(point_angle)
        
        # Sort the angles so that we can do the 2 pointer solution
        angles.sort()
        # Make the array circular so that points in the first quadrant will be included when looking at points in the fouth quadrant 
        angles += [cur_angle + 2 * math.pi for cur_angle in angles]
        # Convert the angle to radians
        angle *= math.pi / 180
        
        max_points = 0
        start = 0

        # Use 2 pointers to find the most number of angles you can fix into your field of view
        for end in range(len(angles)):
            while angles[end] - angles[start] > angle:
                start += 1
            max_points = max(max_points, end - start + 1)
        
        return max_points + extra