class Solution:
    def validPalindrome(self, s: str) -> bool:
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
            
  
        