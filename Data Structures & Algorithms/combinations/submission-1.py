class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        def backtrack(i, subset):
            if len(subset) == k:
                result.append(subset.copy())
                return
            if i == len(nums):
                return
            # consider no backtrack
            backtrack(i+1 , subset)
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop() 
        backtrack(0,[])
        return result

