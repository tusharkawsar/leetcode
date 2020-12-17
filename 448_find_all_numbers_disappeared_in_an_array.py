class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret_val = []
        # if len(nums) == 0:
        #     return ret_val
        
        for index, item in enumerate(nums):
            idx = abs(item) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            
        for index, item in enumerate(nums):
            if item > 0:
                ret_val.append(index+1)
            else:
                nums[index] *= -1
        # print(nums)
        
        return ret_val
            
        