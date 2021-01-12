class NumArray:

#     MY SOLUTION
#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, i: int, j: int) -> int:
#         return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


#     DP
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        
        if self.size:
            # build prefix sum table when input nums is valid
            self.prefix_sum = [ 0 for _ in range(self.size) ]

            self.prefix_sum[0] = nums[0]
            
            # prefix_Sum[k] = nums[0] + ... + nums[k]
            # prefix_Sum[k] = prefix_Sum[k-1] + nums[k]
            for k in range(1,self.size):
                self.prefix_sum[k] = self.prefix_sum[k-1] + nums[k]
        

    def sumRange(self, i: int, j: int) -> int:
        
        # reject query with invalid index
        if self.size == 0 or i < 0 or i > j or j >= self.size:
            return 0
        
        # lookup table from prefix_Sum
        if i == 0:
            return self.prefix_sum[j]
        else:
            return self.prefix_sum[j]-self.prefix_sum[i-1]
