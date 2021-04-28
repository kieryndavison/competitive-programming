/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canPartitionKSubsets = function(nums, k) {
    const sumNums = nums.reduce((a, b) => a + b, 0);
    if (sumNums % k !== 0 || nums.length < k) return false;

    return canPartition(nums, new Array(nums.length), k, 0, 0, sumNums / k);
};

var canPartition = function(nums, used, k, start, curSum, subSum) {
    if (k === 1) return true;
    if (curSum > subSum) return false;
    if (curSum === subSum) return canPartition(nums, used, k - 1, 0, 0, subSum);

    for (var i = start; i < nums.length; i++) {
        if (!used[i]) {
            used[i] = true;
            if (canPartition(nums, used, k, i + 1, curSum + nums[i], subSum)) return true;
            used[i] = false;
        }
    }

    return false;
};