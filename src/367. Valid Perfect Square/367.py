class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        return False

    def isPerfectSquare1(self, num: int) -> bool:
        i = num
        while i * i > num:
            i = (i + num / i) // 2
        return i * i == num


if __name__ == "__main__":
    num = 16
    print(Solution().isPerfectSquare(num))
    print(Solution().isPerfectSquare1(num))
