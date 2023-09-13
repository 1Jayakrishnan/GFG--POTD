class Solution:
    def findLargest(self, N, S):
        # code here
          # Handle special cases where it's not possible
        if S < 0 or (S == 0 and N > 1) or S > 9 * N:
            return "-1"

        result = ['0'] * N

        # Fill the most significant digits first
        for i in range(N):
            if S >= 9:
                result[i] = '9'
                S -= 9
            else:
                result[i] = chr(ord('0') + S)
                break

        return ''.join(result)
