class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            if (height[l] < height[r]) {
                maxarea = Math.max(maxarea, height[l]*(r-l));
                l++;
            } else {
                maxarea = Math.max(maxarea, height[r]*(r-l));
                r--;
            }
        }
        return maxarea;
    }
    public static void main(String[] args) {
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        Solution s = new Solution();
        int ans = s.maxArea(height);
        System.out.println(ans);
        System.out.println(new Solution().maxArea(height));
        
    }
}

