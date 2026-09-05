class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = {}

        def lis(index: int, previous_index: int) -> int:
            if index == len(nums):
                return 0

            state = (index, previous_index)
            if state in memory:
                return memory[state]

            do_not_take = lis(index + 1, previous_index)
            take = 0
            if previous_index == -1 or nums[index] > nums[previous_index]:
                take = 1 + lis(index + 1, index)

            memory[state] = max(take, do_not_take)
            return memory[state]

        return lis(0, -1)


        