from functools import cmp_to_key

class Solution:

    def findLargest(self, arr):
        # Convert all numbers to string for concatenation comparison
        arr = list(map(str, arr))

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come before b
            elif a + b < b + a:
                return 1    # b should come before a
            else:
                return 0

        # Sort with custom comparator
        arr.sort(key=cmp_to_key(compare))

        # Join the result
        result = ''.join(arr)

        # Edge case: if result starts with '0', that means all were zeros
        return '0' if result[0] == '0' else result
