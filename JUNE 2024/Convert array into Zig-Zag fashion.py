from typing import List

class Solution:
    def zigZag(self, n: int, arr: List[int]) -> None:
        for i in range(n - 1):
            if i % 2 == 0:
                # Ensure arr[i] < arr[i + 1]
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                # Ensure arr[i] > arr[i + 1]
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
