class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}

        def dfs(i, cur_sum):

            if i == len(nums):
                return 1 if cur_sum == target else 0

            if (i, cur_sum) in mem:
                return mem[(i, cur_sum)]

            plus = dfs(i + 1, cur_sum + nums[i])
            minus = dfs(i + 1, cur_sum - nums[i])

            mem[(i, cur_sum)] = plus + minus

            return mem[(i, cur_sum)]

        return dfs(0, 0)