class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        safe = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in safe:
                return [safe[complement],i]

            safe[nums[i]] = i
        return []