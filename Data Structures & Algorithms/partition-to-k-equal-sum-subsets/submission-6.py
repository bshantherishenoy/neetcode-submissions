class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k == 0:
            target = total//k
            count = 0
            used = [False]*len(nums)
            if max(nums) > target:
                return False
            nums.sort(reverse=True)
            def backtracking(index, subset_sum, count):
                if count == k:
                    return True
                if subset_sum == target:
                    return backtracking(0, 0, count + 1)
                for i in range(len(nums)):
                    if used[i]:
                        continue
                    if subset_sum + nums[i] > target:
                        continue
                    if i > index and nums[i] == nums[i - 1] and not used[i- 1]:
                        continue
                    used[i] = True
                    if backtracking(i,subset_sum+nums[i],count):
                        return True
                    used[i] = False
                return False
            return backtracking(0,0, count)

        else:
            return False
        