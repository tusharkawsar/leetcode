class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return [key for key in freq.keys() if freq[key]>1]
        
