from typing import List


class Solution:
    def pairsum(self, arr):
        # print(type(arr))
        # code here
        first_max = second_max = float('-inf')
        
        # Traverse through all elements of the array
        for num in arr:
            if num > first_max:
                second_max = first_max  # Update second max
                first_max = num         # Update first max
            elif num > second_max:
                second_max = num         # Update second max
        
