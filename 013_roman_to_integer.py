class Solution:
    def romanToInt(self, s: str) -> int:
        # My Solution
        # mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # sum = 0
        # sub = 1

        # for i in range(len(s)-1):
        #     if s[i] == 'I' and s[i+1] in ('V', 'X'):
        #         sub = -1
        #     elif s[i] == 'X' and s[i+1] in ('L', 'C'):
        #         sub = -1
        #     elif s[i] == 'C' and s[i+1] in ('D', 'M'):
        #         sub = -1

        #     sum += sub * mapping[s[i]]
        #     print(sum)
        #     sub = 1

        # sum += mapping[s[-1]]

        # return sum

        # Better Solution
        res, prev = 0, 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:          # rev the s
            if dict[i] >= prev:
                # sum the value iff previous value same or more
                res += dict[i]
            else:
                # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
                res -= dict[i]
            prev = dict[i]
        return res
