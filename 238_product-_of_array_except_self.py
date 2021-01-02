class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        L, R = [1], [1]
        
        mul = 1
        for i in range(1, len(nums)):
            mul *= nums[i-1] 
            L.append(mul)
        mul = 1
        for i in range(len(nums)-2, -1, -1):
            mul *= nums[i+1] 
            R.insert(0, mul)
            
        for i in range(len(nums)):
            output.append(L[i]* R[i])
        return output
