public class Solution {

    public int maxProfit(int[] prices) {
        int res = 0;
        int len = prices.length;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - prices[i-1] > 0) {
                res += prices[i] - prices[i-1]  ;
            }
        }
        return res;
    }
}
