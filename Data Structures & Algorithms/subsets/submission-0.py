class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total = []
        def backtracking(i, subset):
            nonlocal total
            if i == len(nums):
                result = subset.copy()
                total.append(result)
                return 
            # do not consider
            backtracking(i+1, subset)
            # consider the number
            subset.append(nums[i])
            backtracking(i+1, subset)
            # revert back the consider
            subset.pop()
        backtracking(0,[])
        return total






        