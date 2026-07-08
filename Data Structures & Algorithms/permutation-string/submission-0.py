class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        k = len(s1)
        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i], 0  )+1
        left = 0 
        print(count_s1)
        window_s2 = {}
        for right in range(len(s2)):
            window_s2[s2[right]] = window_s2.get(s2[right],0) +1
            print(window_s2)
            if right - left +1 > k:
                window_s2[s2[left]] -= 1
                if window_s2[s2[left]] == 0:
                    del window_s2[s2[left]]
                left +=1
                
            if window_s2 == count_s1:
                return True
        return False
        