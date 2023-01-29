package main

import "fmt"

// func minOperations(boxes string) []int {
// 	ans := make([]int, len(boxes))
// 	for i := range boxes {
// 		for j, c := range boxes {
// 			if c == '1' {
// 				ans[i] += abs(j - i)
// 			}
// 		}
// 	}
// 	return ans
// }

func minOperations(boxes string) []int {
	left := int(boxes[0] - '0')
	right := 0
	operations := 0
	n := len(boxes)
	for i := 1; i < n; i++ {
		if boxes[i] == '1' {
			right++
			operations += i
		}
	}
	ans := make([]int, n)
	ans[0] = operations
	for i := 1; i < n; i++ {
		operations += left - right
		if boxes[i] == '1' {
			left++
			right--
		}
		ans[i] = operations
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func main() {
	var boxes string = "110"
	fmt.Println(minOperations(boxes))
}
