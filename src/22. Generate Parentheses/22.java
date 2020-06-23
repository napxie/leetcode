class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        if (n == 0) {
            return res;
        }
        dfs("", 0, 0, n, res);
        return res;
    }
    private void dfs(String curStr, int left, int right, int n, List<String> res) {
        if (left == n && right == n) {
            res.add(curStr);
            return;
        }
        if (left < right) {
            return;
        }
        if (left < n) {
            dfs(curStr+"(", left+1, right, n, res);
        }
          if (right < n) {
                dfs(curStr+")", left, right+1, n, res);
            }
    }
}