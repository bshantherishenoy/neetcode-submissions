class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # idea here is to get the max coins 
        # associate every coin to its left and right value 
        
        nums = [1] + nums + [1]
        n = len(nums)
        mem = {}
        def dfs(left, right):
            if left + 1 ==  right:
                return 0 
            ans = 0
            if (left,right) in mem:
                return mem[(left,right)]
            for k in range(left+1,right):
                coins = nums[left] * nums[k] * nums[right]
                nl = dfs(left, k)
                nr = dfs(k,right)
                total = nl + coins +nr 
                ans = max(ans,total)
            mem[(left,right)] = ans
            return ans

        
        return dfs(0, n-1)