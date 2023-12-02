class Solution:
    def isRepresentingBST(self, arr, N):
        # Check if the array is sorted
        for i in range(1, N):
            if arr[i] <= arr[i-1]:
                return 0

        # If the array is sorted, it may still represent a BST
        # Check if there is a valid binary search tree structure
        stack = []
        root = float('-inf')

        for num in arr:
            while stack and num > stack[-1]:
                root = stack.pop()

            if num < root:
                return 0

            stack.append(num)

        return 1
