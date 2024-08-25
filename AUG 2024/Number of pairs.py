from bisect import bisect_right

class Solution:
    
    # Function to count number of pairs such that x^y is greater than y^x.
    def countPairs(self, arr, brr):
        # Sorting brr for binary search
        brr.sort()
        
        # Precompute counts for y <= 4
        countY = [0] * 5
        for y in brr:
            if y < 5:
                countY[y] += 1
        
        count = 0
        n = len(brr)
        
        for x in arr:
            if x == 0:
                # 0^y is always 0 and hence 0^y < y^0 for y > 0
                continue
            elif x == 1:
                # 1^y is always 1 and hence only 1^0 > 0^1
                count += countY[0]
                continue
            
            # Use binary search to find the count of elements in brr which are greater than x
            idx = bisect_right(brr, x)
            count += n - idx
            
            # Special handling for x=2
            if x == 2:
                # Remove counts of y=3 and y=4 since 2^3 < 3^2 and 2^4 < 4^2
                count -= countY[3] + countY[4]
            
            # Special handling for x=3
            if x == 3:
                # Add count of y=2 since 3^2 > 2^3
                count += countY[2]
            
            # Include count of y=0 and y=1 for all x > 1 since x^0 > 0^x and x^1 > 1^x
            count += countY[0] + countY[1]
        
        return count
