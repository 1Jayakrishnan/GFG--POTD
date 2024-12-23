class Solution:
    # Function to search a given number in row-wise sorted matrix
    def searchRowMatrix(self, mat, x):
        # Loop through each row in the matrix
        for row in mat:
            # Apply binary search on the row
            low, high = 0, len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == x:
                    return True
                elif row[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
