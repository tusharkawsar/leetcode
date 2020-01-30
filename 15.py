#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

# https://leetcode.com/problems/3sum/
import collections
def is_duplicate(listoflists, newlist):
    if len(listoflists)==0: return False
    for i in listoflists:
        if collections.Counter(i) == collections.Counter(newlist):
            # print("found a match", newlist)
            return True
    return False

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # print(nums)
        for i in range(0,len(nums)-2,1):
            # print("i =", i, "===========================")
            # find = 0-nums[i]
            # print(find)
            if nums[i]>0: break
            if nums[i] == nums[i-1]: continue
            l = i+1
            r = len(nums)-1
            # print(nums[i], nums[l], nums[r])
            # print("sum = ", find+nums[l]+nums[r])
            while l<=r:
                sum = nums[i]+nums[l]+nums[r]
                # print("sum = ", sum)
                candidate = [nums[i], nums[l], nums[r]]
                if sum==0 and not is_duplicate(result,candidate):
                    result.append(candidate)
                    # print("one appended")
                    l = l+1
                    r = r-1
                elif sum>0:
                    r = r-1
                else:
                    l = l+1
        return result
                
    
# https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)


sol = Solution()
# print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
# print(sol.threeSum([-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6]))
print(sol.threeSum([12,5,-12,4,-11,11,2,7,2,-5,-14,-3,-3,3,2,-10,9,-15,2,14,-3,-15,-3,-14,-1,-7,11,-4,-11,12,-15,-14,2,10,-2,-1,6,7,13,-15,-13,6,-10,-9,-14,7,-12,3,-1,5,2,11,6,14,12,-10,14,0,-7,11,-10,-7,4,-1,-12,-13,13,1,9,3,1,3,-5,6,9,-4,-2,5,14,12,-5,-6,1,8,-15,-10,5,-15,-2,5,3,3,13,-8,-13,8,-5,8,-6,11,-12,3,0,-2,-6,-14,2,0,6,1,-11,9,2,-3,-6,3,3,-15,-5,-14,5,13,-4,-4,-10,-10,11]))

# [-15,10,0,-2,14,-1,-10,-14,10,12,6,-6,10,2,-11,-9,2,13,2,-9,-14,-12,-10,-12,13,13,-10,-3,2,-11,3,-6,6,10,7,5,-13,4,-2,12,1,-11,14,-4,6,-12,-6,-14,8,11,-8,1,7,-3,5,5,-13,10,9,-3,6,-10,6,-3,7,-9,-13,9,10,0,-1,-11,4,-10,-8,-13,-15,2,-12,8,-2,-12,-14,-10,-8,6,2,-5,-7,-11,7,14,-6,-10,-12,8,-4,-10,-5,14,-3,9,-12,8,14,-13]

































# Brute Force - Time limit excedded - BELOW
# =============================================================================
# def is_duplicate(listoflists, newlist):
#     if len(listoflists)==0: return False
#     for i in listoflists:
#         if collections.Counter(i) == collections.Counter(newlist):
#             print("found a match", newlist)
#             return True
#     return False
# 
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         # print(nums)
#         for i in range(0,len(nums)-2,1):
#             for j in range(i+1,len(nums)-1,1):
#                 for k in range(j+1,len(nums),1):
#                     candidate_list = [nums[i],nums[j],nums[k]]
#                     print(candidate_list)
#                     if nums[i]+nums[j]+nums[k]==0 and not is_duplicate(result, candidate_list):
#                         result.append(candidate_list)
#         # print(collections.Counter(result[0]) == collections.Counter(result[2]))
#         return result
# =============================================================================
