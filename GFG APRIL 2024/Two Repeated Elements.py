class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        seen = set()
        repeating_numbers = []
        
        for num in arr:
            if num in seen:
                repeating_numbers.append(num)
            else:
                seen.add(num)
        
        return tuple(repeating_numbers)
