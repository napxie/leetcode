var table []string = []string {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    result := []string{""}
    for i := 0; i < len(digits); i++ {
        t := table[digits[i] - '0']
        temp := []string{}
        for j := 0; j < len(t); j++ {
            for z := 0; z < len(result); z++ {
                temp = append(temp, result[z] + string([]byte{t[j]}))
            }
        }
        result = temp
    }
    return result
}


var digitMap = map[string]string{"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
	"6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
var combinations []string

func letterCombinations(digits string) []string {
	if len(digits)==0 {
        return nil
	}
	
    combinations = []string{}  // 重置全局变量
	getCombinations(digits, 0, "")
	return combinations
}

func getCombinations(digits string, index int, str string) {
	if index==len(digits) {
		combinations = append(combinations, str)
		return 
	}

	for _, s := range []rune(digitMap[digits[index:index+1]]) {
		getCombinations(digits, index+1, str+string(s))
	}
}

