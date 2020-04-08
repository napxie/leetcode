func climbStairs(n int) int {
    res := make([]int, n+1)
    res[0] = 1
    res[1] = 1
    for i := 2; i <= n; i++ {
        res[i] = res[i-1] + res[i-2]
    }
    return res[n]
}

func climbStairs1(n int) int {
    curr, a, b := 1, 1, 1
    for i := 2; i <= n; i++ {
        curr = a + b
        a = b
        b = curr
    }
    return curr
}