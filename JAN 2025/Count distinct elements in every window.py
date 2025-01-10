class Solution:
    def countDistinct(self, arr, k):
        if k > len(arr):
            return []
        
        freq_map = {}
        result = []
        
        # Initialize the first window
        for i in range(k):
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
        
        # Add the count of distinct elements in the first window
        result.append(len(freq_map))
        
        # Slide the window
        for i in range(k, len(arr)):
            # Add the new element
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
            
            # Remove the element that slid out of the window
            freq_map[arr[i - k]] -= 1
            if freq_map[arr[i - k]] == 0:
                del freq_map[arr[i - k]]
            
            # Append the count of distinct elements
            result.append(len(freq_map))
        
        return result
