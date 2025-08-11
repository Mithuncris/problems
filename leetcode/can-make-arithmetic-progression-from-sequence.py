class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        if len(arr)<=1: return True
        arr.sort()

        d = arr[1]-arr[0]
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] != d:
                return False
        return True