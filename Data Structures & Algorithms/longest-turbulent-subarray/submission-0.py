class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        ans = 1

        for right in range(1, len(arr)):
            if arr[right] == arr[right - 1]:
                left = right

            elif right == 1:
                pass

            elif (arr[right] - arr[right - 1]) * \
                 (arr[right - 1] - arr[right - 2]) > 0:
                # Same direction: both positive or both negative
                left = right - 1

            ans = max(ans, right - left + 1)

        return ans