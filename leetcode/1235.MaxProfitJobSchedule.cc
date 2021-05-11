class Solution {
    // Structure for the jobs, contains start and end times and profit
    struct Job {
        Job(): start(0), end(0), profit(0) {}
        Job(int s, int e, int p) : start(s), end(e), profit(p) {}
        int start;
        int end;
        int profit;
    };

    // Comparator used to sort array of Jobs by end time ascending 
    struct JobComparator {
        bool operator()(const Job& a, const Job& b) const { 
            return a.end < b.end;
        }
    };
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        
        // Fixed size array is more efficent than a dynamic vector
        Job jobs[n];

        // Make an array of job structs
        for (int i = 0; i < n; i++) {
            jobs[i] = Job(startTime[i], endTime[i], profit[i]);
        }

        // Sort the array by end times
        sort(jobs, jobs + n, JobComparator());
        
        // Create map to store the max profit for each end time
        map<int,int> maxProfits = {{0, 0}};
        int maxProfit = 0;

        for (auto &job: jobs) {
            // Find the largest job that ends before the current job starts 
            auto firstNonOverlappingJob = prev(maxProfits.upper_bound(job.start));
            
            // Determine the max profit based on the current max and 
            // the profit if the current job is added
            maxProfit = max(maxProfit, firstNonOverlappingJob->second + job.profit);
            maxProfits[job.end] = maxProfit;
        }
        
        return maxProfit;
    }
};