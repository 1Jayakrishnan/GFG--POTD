class Solution:
    def CombinationSum2(self, arr, n, k):
        # code here
        arr.sort()
        result = []
        
        # Helper function to backtrack and find combinations
        def backtrack(start, target, path):
            if target == 0:
                # Add the combination to the result
                result.append(path)
                return
            
            for i in range(start, len(arr)):
                # Skip duplicates
                if i > start and arr[i] == arr[i - 1]:
                    continue
                # If current element is greater than target, break the loop
                if arr[i] > target:
                    break
                # Recursively find combinations with updated parameters
                backtrack(i + 1, target - arr[i], path + [arr[i]])
        
        # Start backtracking from index 0
        backtrack(0, k, [])
        
        return result
