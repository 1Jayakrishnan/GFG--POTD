class Solution:
    def armstrongNumber (self, n):
        # code here 
        # Extract digits
        hundreds = n // 100
        tens = (n // 10) % 10
        ones = n % 10
        
        # Calculate sum of cubes of digits
        sum_of_cubes = (hundreds ** 3) + (tens ** 3) + (ones ** 3)
        
        # Check if the sum of cubes is equal to the number itself
        if sum_of_cubes == n:
            return "Yes"
        else:
            return "No"
