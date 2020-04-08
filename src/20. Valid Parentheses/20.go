func isValid(s string) bool {
    stack := make([]byte, 0, len(s))

    for _, c := range []byte(s) {
        if c == '(' || c == '[' || c == '{' {
            stack = append(stack, c)
            continue
        }

        if len(stack) == 0 {
            return false
        }

        if c == ')' && stack[len(stack)-1] != '(' ||
           c == ']' && stack[len(stack)-1] != '[' ||
           c == '}' && stack[len(stack)-1] != '{' {
                return false
        }
        stack = stack[:len(stack)-1]
    }

    return len(stack) == 0    
}