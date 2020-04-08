
func findMin(nums []int) int {
    l,r := 0, len(nums)-1
    for nums[l] >= nums[r] && l < r {
        mid := l + (r-l) / 2
        if nums[mid] > nums[l]{
            l= mid + 1
        }else if nums[mid] < nums[l]{
            r = mid
        }else{
            l++
        }
    }
    return nums[l]
}


func findMin(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }
    left, right := 0, len(nums) - 1
    if nums[0] < nums[right] {
        return nums[0]
    }
    for left <= right {
        mid := left + (right-left) / 2
        if nums[mid+1] < nums[mid] {
            return nums[mid+1]
        }
        if nums[mid] < nums[mid-1] {
            return nums[mid]
        }
        if nums[0] < nums[mid] {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return nums[left]
}