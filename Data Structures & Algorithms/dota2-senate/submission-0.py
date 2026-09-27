class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = deque()
        dire = deque()

        # Put the positions of each senator into their queue
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # R acts first and bans D
                radiant.append(r + n)
            else:
                # D acts first and bans R
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"