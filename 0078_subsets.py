class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = [[]]
        
        for n in nums:
            l += [[n]+item for item in l]
        
        return l
