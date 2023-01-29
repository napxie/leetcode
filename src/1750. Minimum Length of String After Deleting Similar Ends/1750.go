func minimumLength(s string) int {
	left, right := 0, len(s)-1
	for left < right && s[left] == s[right] {
		c := s[left]
		for left <= right && s[left] == c {
			left++
		}
		for right >= left && s[right] == c {
			right--
		}
	}
	return right - left + 1
}
