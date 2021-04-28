class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> map(60, 0);
        int numPairs = 0;

        for (int i = 0; i < time.size(); i++) {
            int rem = time[i] % 60;
            int pair = (60 - rem) % 60;
            numPairs += map[pair];
            map[rem]++;
        }   

        return numPairs;     
    }
};