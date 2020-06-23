class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int x = 1;
        int y = 2;
        for (int i = 3; i <= n; i++) {
            int temp = x + y;
            x = y;
            y = temp;
        }
        return y;
    }
    public static void main(String[] args) {
        int n = 3;
        System.out.println(n);
    }
}