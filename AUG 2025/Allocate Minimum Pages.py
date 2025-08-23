class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        if k > n:  # Not enough books
            return -1

        # Function to check if allocation is possible with maxPages limit
        def is_possible(limit):
            students = 1
            pages = 0
            for book in arr:
                # early fail
                if book > limit:
                    return False
        
                if pages + book > limit:
                    students += 1
                    pages = book
                    if students > k:   # early stop
                        return False
                else:
                    pages += book
        
            return True

        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                high = mid - 1  # Try for smaller maximum
            else:
                low = mid + 1   # Increase limit

        return result

