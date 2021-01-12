class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for item in nums:
            if item in freq:
                return item
            freq[item] = 1
        
