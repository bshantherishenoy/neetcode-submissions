class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(i, subset):
            nonlocal total
            if i == len(nums):
                xor = 0
                for i in subset:
                    xor ^=i 
                total += xor 
                return 
            # consider to not to take
            backtrack(i+1, subset)
            # consider to take 
            subset.append(nums[i])
            backtrack(i+1, subset)
            # Rever the changes back 
            subset.pop()

        backtrack(0,[])
        return total