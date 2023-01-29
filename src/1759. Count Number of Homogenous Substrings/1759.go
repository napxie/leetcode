func countHomogenous(s string) (res int) {
	const mod int = 1e9 + 7
	prev := rune(s[0])
	cnt := 0
	for _, c := range s {
		if c == prev {
			cnt++
		} else {
			res += (cnt + 1) * cnt / 2
			cnt = 1
			prev = c
		}
	}
	res += (cnt + 1) * cnt / 2
	return res % mod
}
