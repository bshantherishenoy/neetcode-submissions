class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0 
        left = 0 
        for i in s:
            if i in window:
                while window and i in window:
                    window.remove(s[left])
                    left +=1
        
            window.add(i)
            total = len(window)
            max_length = max(total, max_length)
        return max_length
        