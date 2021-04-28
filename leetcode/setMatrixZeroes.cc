#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        //check if first row has a 0
        bool firstRowZero = false;
        for (int i = 0;  i < matrix[0].size(); i++) {
            if (!matrix[0][i]) firstRowZero = true;
        }

        //set rows to zero and set up first row as flag vars
        bool curRowZero = false;
        for (int i = 1;  i < matrix.size(); i++) {
            for (int j = 1; j < matrix[i].size(); j++) {
                if (!matrix[i][j]) {
                    curRowZero = true;
                    matrix[0][j] = 0;
                }
            }
            if (curRowZero) {
                curRowZero = false;
                for (int k = 0; k < matrix[i].size(); k++) {
                    matrix[i][k] = 0;
                }
            }
        }

        //set columns to 0 based on first row
        for (int i = 0;  i < matrix[0].size(); i++) {
            if (!matrix[0][i]) {
                for (int k = 0; k < matrix.size(); k++) {
                    matrix[k][i] = 0;
                }
            }
        }

        //if first row had a 0 set it to 0
        if (firstRowZero) {
            for (int i = 0;  i < matrix[0].size(); i++) {
                matrix[0][i] = 0;
            }
        }
    }
};