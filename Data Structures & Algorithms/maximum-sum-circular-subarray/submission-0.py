class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # keep an index as visited 
        # use the first index mark it as visited 
        # go throgh the enire array as nums[i+1]%n
        # do the same kadane 
        # keep going untill you see the visited number 
        # finally you get the max array 
        n = len(nums)
        ans = nums[0]

        for start in range(n):

            visited = set()
            cur_sum = 0
            i = start

            while i not in visited:
                visited.add(i)

                cur_sum = max(nums[i], cur_sum + nums[i])
                ans = max(ans, cur_sum)

                i = (i + 1) % n

        return ans