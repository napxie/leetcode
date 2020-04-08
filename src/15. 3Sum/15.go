func threeSum(nums []int) [][]int {
    var res [][]int
    sort.Ints(nums)
    for i := 0; i < len(nums)-2; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        target, l, r := -nums[i], i+1, len(nums)-1
        for l < r {
            sum := nums[l] + nums[r]
            if sum == target {
                res = append(res, []int{nums[i], nums[l], nums[r]})
                for l < r && nums[l] == nums[l+1] {
                    l++
                }
                for l < r && nums[r] == nums[r-1] {
                    r--
                }
                l++
                r--                
            } else if sum > target {
                r--
            } else {
                l++
            }
        }
    }
    return res
}