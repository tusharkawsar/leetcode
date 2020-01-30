#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:07:04 2020

@author: tushar
"""
from typing import List


class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_limit = right_limit = -1
        left_limit = self.binarySearch(nums, 0, len(nums), target, 1)
        right_limit = self.binarySearch(nums, 0, len(nums), target, 2) 
        print( [left_limit, right_limit])
        # pass
    
    
    
    
    def binarySearch (self, arr, l, r, x, left_right): 
        # Check base case 
        if r >= l : 
            mid = int(l + (r - l)//2)
            if mid>=len(arr): return -1
            # If element is present at the middle itself 
            if arr[mid] == x:
                
                if left_right==1:
                    if mid==0 or arr[mid-1]<arr[mid]:
                        return mid 
                    else: return self.binarySearch(arr, l, mid-1, x, left_right) 
                elif left_right==2:
                    if mid==len(arr)-1 or arr[mid+1]>arr[mid]:
                        return mid 
                    else: return self.binarySearch(arr, mid+1, r, x, left_right) 
            # If element is smaller than mid, then it can only 
            # be present in left subarray 
            elif arr[mid] > x: 
                return self.binarySearch(arr, l, mid-1, x, left_right) 
            # Else the element can only be present in right subarray 
            else: 
                # print('hello')
                return self.binarySearch(arr, mid+1, r, x, left_right)
        else: 
            # Element is not present in the array 
            return -1
        
solution = Solution()
solution.searchRange([4,4,5,8,8,8,10,10], 10)