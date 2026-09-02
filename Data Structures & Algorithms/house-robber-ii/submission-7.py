class Solution:
    def rob(self, nums: List[int]) -> int:
        # avoid the circle formation all together 
        # check if we can rob form 0 to n-2
        # check if we rob form 1 to n-1 
        n = len(nums)
        if n == 1:
            return nums[0]
        def check(start, end):
            mem = {}
            def rob(i):
                if i >end:
                    return 0
                if i in mem:
                    return mem[i]
                take = nums[i] + rob(i+2)
                skip = rob(i+1)
                mem[i] = max(take, skip)
                return mem[i]
            return rob(start)
        
        return max(check(0,n-2 ), check(1, n-1))
        
        