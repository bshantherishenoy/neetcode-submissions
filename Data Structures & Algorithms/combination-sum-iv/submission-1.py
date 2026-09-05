class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem  = {}
        def dfs(target):
            if target == 0:
                return 1
            if target in mem:
                return mem[target]
            count = 0 
            for num in nums:
                if num <= target:
                    count +=dfs(target-num)
            mem[target] = count
            return mem[target]

        return dfs(target)
        

        