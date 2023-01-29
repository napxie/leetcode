func minimumSize(nums []int, maxOperations int) int {
	max := 0
	for _, x := range nums {
		if x > max {
			max = x
		}
	}
	return sort.Search(max, func(y int) bool {
		if y == 0 {
			return false
		}
		ops := 0
		for _, x := range nums {
			ops += (x - 1) / y
		}
		return ops <= maxOperations
	})
}

