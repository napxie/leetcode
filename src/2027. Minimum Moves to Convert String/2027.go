func minimumMoves(s string) (res int) {
	covered := -1
	for i, c := range s {
		if c == 'X' && i > covered {
			res++
			covered = i + 2
		}
	}
	return
}

func minimumMoves(s string) (ans int) {
	for i := 0; i < len(s); i++ {
		if s[i] == 'X' {
			ans++
			i += 2
		}
	}
	return
}



