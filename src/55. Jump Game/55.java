class Solution {
    public boolean canJump(int[] nums) {
        int max_i = 0, n = nums.length ;
        for (int i = 0; i < n; i ++) {
            if (max_i >= i && i + nums[i] > max_i) {
                max_i = i + nums[i];
            }
        }
        return max_i >= n - 1;
    }
}