func mySqrt(x int) int {
    if x <= 1 {
        return x
    }
    l, r := 1, x / 2
    for l < r {
        var m int
        m = (l+r+1) >> 1
        if m * m > x {
            r = m - 1
        } else {
            l = m
        }
    }
    return l
}

func mySqrt(x int) int {
    if x < 2 {
      return x  
    }
    y := x / 2
    for y * y > x {
        y = ( y + x / y ) / 2
    }
    return int( y )
}