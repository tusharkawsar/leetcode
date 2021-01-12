import operator as op
from functools import reduce

class Solution:
#     My Solution
#     def ncr(self, n, r):
#         r = min(r, n-r)
#         numer = reduce(op.mul, range(n, n-r, -1), 1)
#         denom = reduce(op.mul, range(1, r+1), 1)
#         return numer // denom  # or / in Python 2
    
#     def climbStairs(self, n: int) -> int:
#         limit_2 = n//2
#         combinations = 1
#         # print(self.ncr(3,2))
#         for i in range(limit_2, 0, -1):
#             limit_1 = n - i*2
#             N = i + limit_1
#             R = i
#             # print(i, limit_1, N, R, self.ncr(N, R))
#             combinations += self.ncr(N, R)
        
#         # print(combinations)
#         return combinations

            
        
#         DP Solution
        def climbStairs(self, n: int) -> int:
            # base cases
            if n <= 0: return 0
            if n == 1: return 1
            if n == 2: return 2

            one_step_before = 2;
            two_steps_before = 1;
            all_ways = 0;

            for i in range(2, n):
                all_ways = one_step_before + two_steps_before;
                two_steps_before = one_step_before;
                one_step_before = all_ways;
            return all_ways;
