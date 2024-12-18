class Solution:
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        def isValid(arr, n, k, mid):
            student_count = 1
            current_pages = 0
            
            for pages in arr:
                if current_pages + pages > mid:
                    student_count += 1  # Allocate to a new student
                    current_pages = pages  # Reset the current allocation
                    if student_count > k:  # If more students are needed than available
                        return False
                else:
                    current_pages += pages
            
            return True

        n = len(arr)
        
        # Edge case: If there are fewer books than students
        if k > n:
            return -1

        # Binary search on the range [max(arr), sum(arr)]
        low = max(arr)
        high = sum(arr)
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if isValid(arr, n, k, mid):  # Check if mid pages allocation is feasible
                result = mid  # Update result
                high = mid - 1  # Try for a smaller maximum
            else:
                low = mid + 1  # Try for a larger maximum
        
        return result
