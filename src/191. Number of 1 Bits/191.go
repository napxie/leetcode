func hammingWeight(num uint32) int {
    count := 0
    for num > 0 {
        num = num & (num-1)
        count ++
    }
    return count  
}

func hammingWeight(num uint32) int {
    var count int
    for num !=0{
        if num & 1 == 1{
            count++
        }
        num >>= 1
    }
    return count
}
