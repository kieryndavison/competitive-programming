class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<bitset<26>> dp = {bitset<26>()};
        int maxLength = 0;
        
        for (auto &str: arr) {
            bitset<26> s1;
            for (char ch: str) {
                s1.set(ch - 'a');
            }
            
            int n = s1.count();
            if (str.size() > n) continue;
            
            for (int i = dp.size() - 1; i >= 0; i--) {
                bitset s2 = dp[i];
                if ((s1 & s2).any()) continue;
                dp.push_back(s1 | s2);
                maxLength = max(maxLength, (int)s2.count() + n);
            }
        }
        
        return maxLength;
    }
};