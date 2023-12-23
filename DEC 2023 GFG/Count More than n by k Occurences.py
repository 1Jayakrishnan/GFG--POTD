class Solution:
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        candidates = {}
        
        # Step 1: Find potential candidates.
        for num in arr:
            if num in candidates:
                candidates[num] += 1
            elif len(candidates) < k - 1:
                candidates[num] = 1
            else:
                # Eliminate pairs of different elements.
                for key in list(candidates.keys()):
                    candidates[key] -= 1
                    if candidates[key] == 0:
                        del candidates[key]
        
        # Step 2: Reset counts for potential candidates.
        for key in candidates.keys():
            candidates[key] = 0
        
        # Step 3: Count occurrences of potential candidates.
        for num in arr:
            if num in candidates:
                candidates[num] += 1
        
        # Step 4: Check and count elements that appear more than n/k times.
        result = 0
        for key in candidates.keys():
            if candidates[key] > n // k:
                result += 1
        
        return result

