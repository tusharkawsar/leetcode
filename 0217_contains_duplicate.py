class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        return False
        
#         More time and space
        # count_dict = {}
        # for item in nums:
        #     if item in count_dict.keys(): # this is O(1)
        #         return True
        #     count_dict[item] = 1
        # return False
        