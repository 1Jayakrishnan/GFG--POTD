class Solution:
    def sumSubMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        prev_less = [0] * n
        next_less = [0] * n
        
        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        # Clear stack for next pass
        stack.clear()
        
        # Next Less Element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Calculate total sum
        result = 0
        for i in range(n):
            left = i - prev_less[i]
            right = next_less[i] - i
            result += arr[i] * left * right
            result %= MOD
        
        return result
