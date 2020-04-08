func moveZeroes(nums []int)  {
	index := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[index] = nums[i]
			index++
		}
	}
	for i := index; i < len(nums); i++ {
		nums[i] = 0
	}
}

func moveZeroes1(nums []int)  {
    i, count := 0, 0
    for i < len(nums)-count {
        if nums[i] == 0 {
            nums = append(append(nums[:i], nums[i+1:len(nums)]...), 0)
            count++
            continue
        } 
        i++
    }
}