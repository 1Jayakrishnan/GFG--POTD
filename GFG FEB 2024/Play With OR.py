class Solution:
    def game_with_number(self, arr, n):
        # Iterate through the array up to the second-to-last element
        for i in range(n - 1):
            # Perform bitwise OR between arr[i] and arr[i+1]
            arr[i] = arr[i] | arr[i + 1]
            
        return arr
