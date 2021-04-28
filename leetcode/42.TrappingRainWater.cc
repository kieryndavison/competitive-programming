class Solution {
public:
    int trap(vector<int>& height) {
        int start = 0, end = height.size() - 1;
        int maxLeft = 0, maxRight = 0;
        int total = 0;

        while (start < end) {
            if (height[start] < height[end]) {
                maxLeft = max(maxLeft, height[start]);
                total+= maxLeft - height[start];
                start++;
            } else {
                maxRight = max(maxRight, height[end]);
                total+= maxRight - height[end];
                end--;
            }
        }

        return total;
    }
};