class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         LINEAR SEARCH
        # for i in range(1, len(arr)-1):
        #     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        #         return i
        
#         BINARY SEARCH
        low, high = 0, len(arr)-1
        
        while low <= high:
            mid = (low+high)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]:
                low = mid
            else:
                high = mid
                
        
