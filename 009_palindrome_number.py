class Solution:
    def isPalindrome(self, x: int) -> bool:
        # SOLUTION USING STRING
        #         x_str = str(x)
        #         if x_str == x_str[::-1]:
        #             return True
        #         return False

        # SOLUTION NOT USING STRING
        if x < 0:
            return False

        x_rev = 0
        x_copy = x
        while x:
            x_rev = x_rev*10 + x % 10
            x //= 10
        print(x_rev, x_copy)
        if x_rev == x_copy:
            return True
        return False
