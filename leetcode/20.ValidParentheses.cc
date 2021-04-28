class Solution {
    map<char,char> parenOptions;
public:
    bool isValid(string s) {
        parenOptions[')'] = '(';
        parenOptions[']'] = '[';
        parenOptions['}'] = '{';
        stack<char> parentheses;

        for (auto ch : s) {
            if (parenOptions.find(ch) != parenOptions.end()) {
                if (parentheses.empty() || parentheses.top() != parenOptions.find(ch)) return false;
                else parentheses.pop();
            } else {
                parentheses.push(ch);
            }
        }
        
        return parentheses.empty() ? true : false;
    }
};