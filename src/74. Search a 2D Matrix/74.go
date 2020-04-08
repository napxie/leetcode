func searchMatrix(matrix [][]int, target int) bool {
    m := len(matrix)
    if m == 0 {
        return false
    }
    n := len(matrix[0])
    left, right := 0, m * n -1
    for left <= right {
        pivot_idx := left + (right - left) / 2
        pivot_element := matrix[pivot_idx/n][pivot_idx%n]
        if target == pivot_element {
            return true
        } else {
            if target < pivot_element {
                right = pivot_idx - 1
            } else {
                left = pivot_idx + 1
            }
        }
    }
    return false
}