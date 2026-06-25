class Solution:
    def validPalindrome(self, s: str) -> bool:
        # O(n) solution check if the 
        # a b c a
        #   ↑ ↑
        #   b c
        # just try to understand this contion ignore left and add right one extra 
        # ignore right and add left one extra.
        left = 0
        n = len(s) 
        right = n - 1
        def is_palli(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        while left < right:
            if s[left] != s[right]:
               return is_palli(left+1, right) or is_palli(left,right-1)
            else:
                left +=1
                right -=1
        return True
            
  
        