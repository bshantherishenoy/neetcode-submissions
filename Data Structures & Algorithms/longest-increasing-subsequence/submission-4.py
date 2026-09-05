class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for number in nums:
            left = 0
            right = len(tails)
            while left < right:
                middle = (left + right) // 2
                if tails[middle] < number:
                    left = middle + 1
                else:
                    right = middle

            if left == len(tails):
                tails.append(number)
            else:
                tails[left] = number

        return len(tails)

        