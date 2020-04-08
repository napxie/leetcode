func reverseBits(num uint32) uint32 {
    res, count := uint32(0), uint32(31)
    for num != 0 {
        res += (num & 1) << count
        num >>= 1
        count -= 1
    }
    return res
}