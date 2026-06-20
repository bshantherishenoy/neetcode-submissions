class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # checking if the length +1 in the set makeing it o(n)
        # compare with the sof far seen numbers
        num_set = set(nums)
        long = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length +=1
                long = max(long,length)
        return long
        