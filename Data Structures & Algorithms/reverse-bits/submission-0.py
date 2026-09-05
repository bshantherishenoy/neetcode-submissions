class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:]
        binary_str = binary_str.zfill(32)

        reversed_str = binary_str[::-1]

        return int(reversed_str, 2)