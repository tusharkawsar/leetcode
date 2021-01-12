class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for item in nums:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        res = dict((v,k) for k,v in count.items())
        print(res)
        x = list(res.keys())
        x.sort()
        print(x)
        return(res[max(x)])
        
