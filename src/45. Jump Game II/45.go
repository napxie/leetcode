func jump(nums []int) int {
    step, end, max_bound := 0, 0, 0
    for i := 0; i < len(nums) - 1; i++ {
        if i + nums[i] > max_bound {
            max_bound = nums[i] + i
        }
        if i == end {
            end = max_bound
            step += 1
            if end >= len(nums) - 1 {
                return step
            }
        }
    }
    return step
}