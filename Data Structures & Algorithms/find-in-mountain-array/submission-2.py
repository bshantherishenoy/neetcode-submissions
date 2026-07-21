class Solution:
    def Binarysearch(self,left,right, target, mountainArr, asce):
        while left <= right :
            mid = (left + right)//2
            value = mountainArr.get(mid)
            if value == target:
                return mid
            if asce:
                if value < target:
                    left = mid+ 1
                else:
                    right = mid-1
            else:
                if value < target:
                    right = mid-1
                else:
                    left = mid + 1
        return -1
                
            

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left = 0
        right = mountainArr.length()-1 
        while left < right:
            mid = (left + right)//2
            if mountainArr.get(mid)< mountainArr.get(mid+1):
                left = mid + 1
            else :
                right = mid
        peak= left
        found=self.Binarysearch(0, peak, target, mountainArr, True)
        if found != -1:
            return found
        return self.Binarysearch(peak+ 1, mountainArr.length()-1,target, mountainArr, False)

     