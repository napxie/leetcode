func isFlipedString(s1 string, s2 string) bool {
	if s1==s2{
		return true
	}
	if len(s1)!=len(s2){
		return false
	}
	return strings.Contains(s1+s1,s2)
}

func isFlipedString(s1 string, s2 string) bool {
    var m = make([]int, 256)
    for _, c := range s1 {
        m[c-'0']++
    }
    for _, c:= range s2 {
        m[c-'0']--
    }
    for _, n := range m {
        if n != 0 {
            return false
        }
    }
    return true
}