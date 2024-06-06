def max_sum(a,n):
    #code here
    S0 = sum(i * a[i] for i in range(n))
    
    # Calculate the total sum of array elements
    sum_a = sum(a)
    
    # Initialize the maximum sum as S0
    max_sum = S0
    
    # Current value of sum
    current_sum = S0
    
    # Iterate to calculate sums for all rotations
    for i in range(1, n):
        # Calculate the new sum using the relationship
        current_sum = current_sum + sum_a - n * a[n - i]
        
        # Update the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
