class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort (events.begin(), events.end());
        int totalDays = 0;
        for (auto event: events) {
            totalDays = max(totalDays, event[1]);
        }
        int totalEvents = 0, curIndex = 0;
        priority_queue <int, vector<int>, greater<int> > pq;

        for (int i = 1; i <= totalDays; i++) {
            if (curIndex < events.size() && pq.empty()) {
                i = events[curIndex][0];
            }

            while (curIndex < events.size() && events[curIndex][0] <= i) {
                pq.push(events[curIndex][1]);
                curIndex++;
            }

            while (!pq.empty() && pq.top() < i) {
                pq.pop();
            }
            
            if (!pq.empty()) {
                pq.pop();
                totalEvents++;
            } else if (curIndex >= events.size()) {
                break;
            }
        }
        return totalEvents;
    }
};