class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        result = []
        for i,c in enumerate(s):
            last[c] = i
        start = 0
        boundry = 0 
        for i,c in enumerate(s):
            boundry = max(boundry, last[c])
            if i == boundry:
                result.append(i-start+1)
                start = i+1
        return result        