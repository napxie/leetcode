func canJump(nums []int) bool {
    maxlen := 0
    for i, jump := range nums {
        if  maxlen >= i && i + jump > maxlen {
            maxlen = i + jump
        }
    }
    return maxlen >= len(nums) - 1
}