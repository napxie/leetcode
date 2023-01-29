func checkIfPangram(sentence string) bool {
	state := 0
	for _, c := range sentence {
		state |= 1 << (c - 'a')
	}
	return state == 1<<26-1
}

func checkIfPangram1(sentence string) bool {
	exist := [26]bool{}
	for _, c := range sentence {
		exist[c-'a'] = true
	}
	for _, b := range exist {
		if !b {
			return false
		}
	}
	return true
}