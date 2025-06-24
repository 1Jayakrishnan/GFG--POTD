class Solution:
    def maxSubseq(self, s, k):
        n = len(s)
        keep = n - k  # number of characters to keep
        stack = []

        for i, ch in enumerate(s):
            # Remove smaller chars from stack if we still can remove
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # Only take the first (n-k) characters
        return ''.join(stack[:keep])
