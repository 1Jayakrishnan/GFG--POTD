class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        # Sort the citations in descending order
        citations.sort(reverse=True)
        
        # Initialize h-index
        h_index = 0
        
        # Iterate through the sorted list
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
