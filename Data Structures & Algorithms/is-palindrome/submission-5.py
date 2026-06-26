class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Nope this time I did not think of using joins and splits:)
        spl = [',','!','?','.','"',"'",":"]
        word = ""
        for w in s:
            if w == " ":
                continue
            else:
                word +=w.lower()
        s = word 
        n = len(s)
        left = 0 
        right = n-1
        while left < right:
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