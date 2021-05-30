class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by start time
        intervals.sort()
        res = []
        
        # Go through all the intervals
        for interval in intervals:
            
            # if the current start time overlaps with the previous end time update 
            # the end time then merge the intervals
            if res and (res[-1][1] >= interval[0]): 
                res[-1][1] = max(res[-1][1], interval[1])
            
            # otherwise add the interval to the list
            else: res.append(interval)
        
        return res