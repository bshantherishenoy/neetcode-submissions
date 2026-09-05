class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):

            if i == len(nums):
                result.append(subset.copy())
                return

            # Take nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # Skip nums[i] and all duplicates of nums[i]
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            backtrack(j, subset)

        backtrack(0, [])
        return result
        