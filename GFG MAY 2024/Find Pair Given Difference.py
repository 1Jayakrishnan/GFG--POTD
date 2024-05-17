from typing import List

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort()
        s = set()
        for i in range(n):
            if arr[i] - x in s or arr[i] + x in s:
                return 1
            s.add(arr[i])
        return -1
