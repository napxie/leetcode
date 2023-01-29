func minElements(nums []int, limit int, goal int) int {
	sum := 0
	for _, x := range nums {
		sum += x
	}
	diff := abs(sum - goal)
	return (diff + limit - 1) / limit
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}