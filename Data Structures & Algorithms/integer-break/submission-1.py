class Solution:
    def integerBreak(self, n: int) -> int:
        mem = {}

        def check(n):
            if n == 1:
                return 1

            if n in mem:
                return mem[n]

            ans = 0

            for i in range(1, n):
                remaining = n - i

                # Either break remaining further,
                # or take remaining as one number
                cur_product = i * max(check(remaining), remaining)

                ans = max(ans, cur_product)

            mem[n] = ans
            return ans

        return check(n)