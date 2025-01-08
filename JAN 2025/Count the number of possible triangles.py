class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n = len(arr)
        count = 0

        # Fix the largest side (c) and use two pointers
        for c in range(n - 1, 1, -1):
            left, right = 0, c - 1
            while left < right:
                # Check if the triangle inequality holds
                if arr[left] + arr[right] > arr[c]:
                    # All pairs (left, left+1, ..., right) form valid triangles
                    count += (right - left)
                    # Move the right pointer to explore smaller triangles
                    right -= 1
                else:
                    # Move the left pointer to explore larger sums
                    left += 1
        
        return count
