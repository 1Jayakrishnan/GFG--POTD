from collections import Counter

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        threshold = n//3
        arr_dict = Counter(arr)
        
        new = [key for key, value in arr_dict.items() if value > threshold]
        #print(arr_dict)
        
        return sorted(new)
