class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        maps = {}
        for truster,trustee in trust:
            if trustee not in maps:
                maps[trustee] = [truster]
            else:
                maps[trustee].append(truster)
        print(maps)
        for key,value in maps.items():
            if len(value) == n-1:
                # Judge cannot trust anyone
                if key not in [truster for truster, trustee in trust]:
                    return key
        return -1

        