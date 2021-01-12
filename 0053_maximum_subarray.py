class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #        BRUTE FORCE
        #         total = -float('inf')

        #         if len(nums) == 1: return nums[0]

        #         for i in range(0, len(nums)):
        #             print("===========")
        #             for j in range(i, len(nums)):
        #                 print(nums[i], nums[j])
        #                 total = max(total, sum(nums[i:j+1]))
        #                 print("sum:", sum(nums[i:j+1]))
        #         return total

        #         KADANE
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
