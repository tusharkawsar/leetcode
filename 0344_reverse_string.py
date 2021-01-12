#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(len_s//2):
            s[i], s[len_s-i-1] = s[len_s-i-1], s[i]
        # return s
    
    
sol = Solution()
# print(sol.reverseString(["h","e","l","l","o"]))
print(sol.reverseString(["H","a","n","n","a","h"]))