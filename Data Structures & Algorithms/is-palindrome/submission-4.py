class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        left = 0 
        right = n-1
        spl = [',','!','?','.','"',"'",":"]
        word = ""
        for w in s:
            if w == " ":
                continue
            else:
                word +=w
        s = word 
        n = len(s)
        left = 0 
        right = n-1
        while left <= n//2 and right >= n//2:
            print(s[left],s[right])
            if s[left] == s[right]:
                left +=1
                right -=1
            elif s[left] in spl:
                left +=1
            elif s[right] in spl:
                right -=1
            else:
                return False
        return True