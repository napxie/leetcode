func search(nums []int, target int) int {
    if len(nums) == 0 {
        return -1
    }
    left, right := 0, len(nums) - 1
    for {
        if left == right {
            if nums[left] == target {
                return left
            }
            return -1
        }
        mid := left + (right-left) / 2
        if nums[left] <= nums[mid] {
            if nums[left] <= target && target <= nums[mid] {
                right = mid
            } else {
                left = mid + 1
            }
        } else {
            if nums[mid] <= target && target <= nums[right] {
                left = mid
            } else {
                right = mid - 1
            }
        }
        
    }
}