class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        fibonacci_sequence = [1, 1]  # Initialize the sequence with the first two numbers
        
        while len(fibonacci_sequence) < n:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate the next Fibonacci number
            fibonacci_sequence.append(next_number)
        
        return fibonacci_sequence[:n]  # Return the first n Fibonacci numbers
