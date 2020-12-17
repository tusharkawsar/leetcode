class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         Using calculation
        # return 2*sum(set(nums)) - sum(nums)
        
#         Using Dict
        dict_nums = {}
        # for item in nums:
        #     if item in dict_nums:
        #         dict_nums[item] += 1;
        #     else:
        #         dict_nums[item] = 1;
        # for key, value in dict_nums.items():
        #     if value == 1:
        #         return key;
        
#         XOR
        result = 0
        for item in nums:
            result ^= item
        return result
