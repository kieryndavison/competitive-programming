class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int letterCount[26]{0};
        
        for (char ch : text) {
            letterCount[ch - 'a']++;
        }
        
        return min({letterCount[1], letterCount[0], letterCount[13], letterCount[11] / 2, letterCount[14] / 2});
    }
};