class Solution:
    def numSteps(self, s: str) -> int:
        if s == '1':
            return 0
        sum, j, count = 0, 0, 0
        for i in s[::-1]:
            sum += int(i) * 2**j
            j += 1
        while sum != 1:
            if sum % 2 == 1:
                sum += 1
            else:
                sum //= 2
            count += 1
        return count


if __name__ == "__main__":
    s = '1101'
    print(Solution().numSteps(s))
