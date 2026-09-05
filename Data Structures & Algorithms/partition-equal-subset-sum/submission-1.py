class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        dp = {}
        if sum_nums %2 == 0:
            total = sum_nums//2
            def dfs(index:int, total:int) -> bool:
                if total == 0:
                    return True
                if index == len(nums) or total<0:
                    return False
                if (index, total) in dp:
                    return dp[(index, total)]
                take = dfs(index+1 , total-nums[index])
                skip = dfs(index+1, total)
                dp[(index, total)] = take or skip

                return dp[(index, total)]
            return dfs(0, total)    
        else:
            return False
        