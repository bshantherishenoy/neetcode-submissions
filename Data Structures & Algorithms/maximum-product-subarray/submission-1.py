class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algorithm 
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            if x < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)

            ans = max(ans, cur_max)
        return ans