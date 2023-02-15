
func isGoodArray(nums []int) bool {
	g := 0
	for _, x := range nums {
		g = gcd(g, x)
		if g == 1 {
			return true
		}
	}
	return false
}

func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

