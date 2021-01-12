class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         Brute Force
        # nums.sort()
        # for index, item in enumerate(nums):
        #     if index != item:
        #         return index
        # return len(nums)
        
#         Dict is slower than sorting
        # dict_nums = {}
        # for item in nums:
        #     dict_nums[item] = 1
        # for i in range(0, len(nums)):
        #     if i not in dict_nums:
        #         return i
        # return len(nums)
    
#     Best Solution
        n = len(nums)
        sum_nums = n * (n+1)/2
        return int(sum_nums - sum(nums))
