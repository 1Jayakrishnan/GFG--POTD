class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        max_zeros_count = 0  # Track the maximum number of zeros
        max_zeros_column = -1  # Track the column with the maximum number of zeros

        for j in range(N):  # Iterate through each column
            zeros_count = 0  # Count of zeros in the current column

            for i in range(N):  # Iterate through each row in the current column
                if arr[i][j] == 0:
                    zeros_count += 1

            # Update max_zeros_column if the current column has more zeros
            if zeros_count > max_zeros_count:
                max_zeros_count = zeros_count
                max_zeros_column = j

        return max_zeros_column
