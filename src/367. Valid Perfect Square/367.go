func isPerfectSquare(num int) bool {
    if num < 2 {
        return true
    }
    left, right := 2, num / 2
    for left <= right {
        var x int
        x = left + (right-left) / 2
        if  x * x == num {
            return true
        } else if  x * x > num {
            right = x - 1
        } else {
            left = x + 1
        }
    }
    return false
}

func isPerfectSquare(num int) bool {
    var i int
    i = num
    for i * i > num {
        i = (i+num/i) / 2
    }
    return i * i == num
}