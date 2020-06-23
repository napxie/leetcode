func maxSlidingWindow(nums []int, k int) []int {
    n := len(nums)

	if n == 0 {
		return make([]int,0)
	}


	i,j := 0,0

	max := nums[i]

	r := make([]int,0)

	pos := 0

	for j < n {

		if nums[j] > max {
			max = nums[j]
			if i + k == j + 1 {
				r = append(r,max)
			}
			pos = j
		} else if i + k == j + 1 {
			r = append(r,max)
		}

		j++

		if (j - i) == k {

			if pos == i && j < n {
				pos++
				max = nums[pos]
				m := pos
				for m < j {
					if nums[m] > max {
						max = nums[m]
						pos = m
					}
                    m++
				}
			}

			i++
		}

	}

	return r
}