class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        element_count = {}

        # Iterate through the array to count occurrences
        for num in a:
            if num in element_count:
                element_count[num] += 1
            else:
                element_count[num] = 1

            # Check if the current element occurs at least k times
            if element_count[num] == k:
                return num

        # If no such element is found
        return -1
