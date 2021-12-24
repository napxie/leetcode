func destCity(paths [][]string) string {
    citiesA := map[string]bool{}
    for _, path := range paths {
        citiesA[path[0]] = true
    }
    for _, path := range paths {
        if !citiesA[path[1]] {
            return path[1]
        }
    }
    return ""
}

