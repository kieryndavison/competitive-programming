class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int>> charsRead;

        for (auto ch : s) {
            if (charsRead.empty() || charsRead.back().first != ch) charsRead.push_back({ch, 0});
            if (++charsRead.back().second == k) charsRead.pop_back();
        }
        
        string ans;
        for (auto & element: charsRead) {
            ans.append(element.second, element.first);
        }
                
        return ans;
    }
};