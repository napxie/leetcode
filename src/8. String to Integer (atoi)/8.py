class Solution:
    def myAtoi(self, str: str) -> int:
        # return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)

        s = list(str.strip())
        if len(s) == 0: 
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in ['-', '+']:
            del s[0]
        ret, i = 0, 0
        while i < len(s) and s[i].isdigit():
            ret = ret * 10 + int(s[i])
            i += 1
        return max(-2**31, min(sign*ret, 2**31-1))

if __name__ == "__main__":
    str = "   -42"
    print(Solution().myAtoi(str))