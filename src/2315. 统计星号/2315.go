func countAsterisks(s string) (res int) {
    valid := true
    for _, c := range s {
        if c == '|' {
            valid = !valid
        } else if c == '*' && valid {
            res++
        }
    }
    return
}