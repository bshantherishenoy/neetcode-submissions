class Solution:
    def validPalindrome(self, s: str) -> bool:
        # excluding the word and joining the entire string again and check its reverse
        # if the reverse is equal to the string itself then return.
        # time complexity of this is o(n^2)
        for i in range(len(s)):
            sim = s[:i] +s[i+1:]
            if sim == sim[::-1]:
                return True
        return False
            
  
        