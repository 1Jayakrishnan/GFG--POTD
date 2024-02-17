class Solution:
    def isMaxHeap(self, arr, n):
        # Traverse the array starting from the last non-leaf node
        # and check the Max Heap property
        for i in range(n // 2 - 1, -1, -1):
            # Check if the current node is greater than or equal to its left child
            if 2 * i + 1 < n and arr[i] < arr[2 * i + 1]:
                return False

            # Check if the current node is greater than or equal to its right child
            if 2 * i + 2 < n and arr[i] < arr[2 * i + 2]:
                return False

        # If the loop completes without returning False, the array is a Max Heap
        return True
