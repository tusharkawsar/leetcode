class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for index, item in enumerate(nums):
            if item in hash_table:
                return [hash_table[item], index]

            hash_table[target-item] = index

        return []

        # Brute force
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums))
        #         if nums[i]+nums[j] == target and i!=j:
        #             return [i, j]
        # return []
