func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    for _, str := range strs {
        b := []byte(str)
        sort.Slice(b, func(i, j int) bool {
            return b[i] < b[j]
        })
        key := string(b)
        groups[key] = append(groups[key], str)
    }
    
    ret := make([][]string, 0, len(groups))
    for _, v := range groups {
        ret = append(ret, v)        
    }
    return ret
}