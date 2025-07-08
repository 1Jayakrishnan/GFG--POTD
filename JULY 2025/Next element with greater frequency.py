from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Pop elements from stack with freq <= current element's freq
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()

            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1

            stack.append(arr[i])

        return res
