func minDistance(word1 string, word2 string) int {
    m, n := len(word1), len(word2)
    dp := make([][]int, m+1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]int, n+1)
        dp[i][0] = i
    }
    for i := 0; i < n + 1; i++ {
        dp[0][i] = i
    }
    dp[0][0] = 0
    for i:= 1; i < m+1; i++ {
        for j := 1; j < n + 1; j++ {
            if word1[i-1] == word2[j-1] {
                dp[i][j] = dp[i-1][j-1]
            } else {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            }
        } 
    }
    return dp[m][n]

}

func min(a, b, c int) int {
    if a > b {
        a = b
    }
    if a > c {
        a = c
    }
    return a
}