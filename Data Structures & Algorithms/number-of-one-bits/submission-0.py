class Solution:
    def hammingWeight(self, n: int) -> int:
        strz= bin(n)
        return strz.count('1')