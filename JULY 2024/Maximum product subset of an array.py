class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7
        
        # Edge case: when arr contains only one element
        if len(arr) == 1:
            return arr[0] % MOD
        
        # Separate positive, negative and zero elements
        positive = []
        negative = []
        zero_count = 0
        
        for num in arr:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero_count += 1
        
        # If there are no positive and no negative numbers, return 0
        if len(positive) == 0 and len(negative) == 0:
            return 0
        
        # Sort the negative numbers to easily manage the count
        negative.sort()
        
        # If there is an odd count of negative numbers, remove the largest (least negative) one
        if len(negative) % 2 != 0:
            negative.pop()
        
        # Calculate the product of the remaining numbers
        product = 1
        
        for num in positive + negative:
            product = (product * num) % MOD
        
        return product
