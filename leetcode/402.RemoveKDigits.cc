class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k == num.length()) return "0";
        string resNum;

        for (int i = 0; i < num.length(); i++) {
            while (k > 0 && !resNum.empty() && resNum.back() > num[i]) {
                resNum.pop_back();
                k--;
            }

            resNum.push_back(num[i]);
        }
        
        while (k > 0){
            resNum.pop_back();
            k--;            
        }

        return resNum.erase(0, min(resNum.find_first_not_of('0'), resNum.size()-1));
    }
};