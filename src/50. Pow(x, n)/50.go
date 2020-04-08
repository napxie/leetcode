func myPow(x float64, n int) float64 {
    if n < 0 {
        x = 1 / x
        n = -n
    }
    pow :=  float64(1)
    for n != 0 {
        if n & 1 == 1 {
            pow *= x
        }
        x *= x
        n >>= 1
    }
    return pow
}

func myPow(x float64, n int) float64 {
    if n == 0 {
        return 1
    }
    if n < 0 {
        return 1 / myPow(x, -n)
    }
    if n % 2 != 0 {
        return x *myPow(x, n-1)
    }
    return myPow(x*x, n/2)
}
