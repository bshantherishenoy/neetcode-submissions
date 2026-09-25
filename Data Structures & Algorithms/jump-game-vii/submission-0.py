class Solution:
        def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
            n = len(s)

            reachable = [False] * n
            reachable[0] = True

            count = 0

            for i in range(1, n):
                # Add the index entering our valid window
                if i - minJump >= 0 and reachable[i - minJump]:
                    count += 1

                # Remove the index leaving our valid window
                if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
                    count -= 1

                # i is reachable if:
                # 1. s[i] is 0
                # 2. there is at least one reachable index in the window
                if s[i] == '0' and count > 0:
                    reachable[i] = True

            return reachable[n - 1]