class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            sim = s[:i] +s[i+1:]
            if sim == sim[::-1]:
                return True
        return False
            
  
        