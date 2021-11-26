class Solution:
    # DP solution
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i in range(len(stations)):
            for j in range(i + 1)[::-1]:
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
            
        for i, fuel in enumerate(dp):
            if fuel >= target:
                return i
            
        return -1

    # Priority Queue solution
    class Solution:
        def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
            pq = []  
            tank = startFuel
            prev = ans = 0
            stations.append([target, float('inf')])
            
            for distance, fuel in stations:
                tank -= distance - prev
                while pq and tank < 0:
                    tank += -heapq.heappop(pq)
                    ans += 1
                
                if tank < 0:
                    return -1
                heapq.heappush(pq, -fuel)
                prev = distance
            
            return ans