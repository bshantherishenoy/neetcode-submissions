class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}
        if n == 1:
            return nums[0]
        def fn(x):
            if x >=n:
                return 0
            if x in mem:
                return mem[x]
            take = nums[x] + fn(x+2)
            skip = fn(x+1)
            mem[x] = max(take, skip)
            return mem[x]
        
        return fn(0)