func removeDuplicates(nums []int) int {
    if len(nums) <= 1 {
        return len(nums)
    }
    j := 1
    for i:=1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            nums[j] = nums[i]
            j++
        }
    }
    return j
}