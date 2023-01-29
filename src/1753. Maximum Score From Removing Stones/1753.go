
func maximumScore(a int, b int, c int) int {
	sum := a + b + c
	maxVal := max(max(a, b), c)
	if sum < maxVal * 2 {
		return sum - maxVal
	}
	return sum / 2
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}