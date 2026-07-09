class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}

        for char in t:
            count[char] = count.get(char, 0) + 1

        left = 0
        missing = len(t)
        result = ""
        for right in range(len(s)):

            if s[right] in count:
                if count[s[right]] > 0:
                    missing -= 1

                count[s[right]] -= 1

            while missing == 0:

                # update answer
                if result == "" or right - left + 1 < len(result):
                    result = s[left:right + 1]

                # remove left character
                if s[left] in count:
                    count[s[left]] += 1

                    if count[s[left]] > 0:
                        missing += 1

                left += 1

        return result
