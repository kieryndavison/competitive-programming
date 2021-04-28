/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    var minSum = nums[0];
    var sum = nums[0];
    nums.forEach((n, i) => {
        if (i < 1) return;
        sum += n;
        minSum = Math.min(minSum, sum);
    });
    
    return minSum >= 1 ? 1 : Math.abs(minSum) + 1;
    
};