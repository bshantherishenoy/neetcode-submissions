class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum  = float('-inf')
        cur_sum = float('-inf')
        for i in nums:
            cur_sum = max(i, cur_sum+i)
            max_sum = max(cur_sum, max_sum)
        return max_sum
        