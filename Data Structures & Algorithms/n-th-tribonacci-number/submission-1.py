class Solution:
    def __init__(self):
        self.mem = {}
    def tribonacci(self, n: int) -> int:
        if n<0:
            return 0
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        elif n in self.mem:
            return self.mem[n]
        else:
            self.mem[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return self.mem[n]
        