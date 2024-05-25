class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        #code here
        max_books = 0
        current_sum = 0
        
        for i in range(n):
            if arr[i] <= k:
                current_sum += arr[i]
                max_books = max(max_books, current_sum)
            else:
                current_sum = 0
        
        return max_books
