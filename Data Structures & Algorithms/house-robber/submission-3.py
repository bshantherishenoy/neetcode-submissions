class Solution:
    def rob(self, nums: List[int]) -> int:
        num_max = 0
        actual_max = 0
        n = len(nums)
        mem = {}
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