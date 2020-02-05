#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = []
        new_list = []
        for i in range(len(nums)):
            if nums[i] != 0:
                new_list.append(nums[i])
            else:
                zero_pos.append(i)
        nums = new_list + [0]*len(zero_pos)
        print(nums)
    
    
    
sol = Solution()
sol.moveZeroes([0,1,0,3,12])

