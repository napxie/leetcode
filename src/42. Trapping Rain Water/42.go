func trap(height []int) int {
    res, idx, stack := 0, 0, make([]int, 0)
    for idx < len(height) {
        for len(stack) != 0 && height[idx] > height[stack[len(stack)-1]] {
            top := stack[len(stack)-1]
            stack = stack[0:len(stack)-1]
            if len(stack) == 0 {
                break
            }
            w := idx - stack[len(stack)-1] - 1
            h := min(height[stack[len(stack)-1]], height[idx]) - height[top]
            res += w * h 
        }
        stack = append(stack, idx)
        idx++
    }
    return res
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}