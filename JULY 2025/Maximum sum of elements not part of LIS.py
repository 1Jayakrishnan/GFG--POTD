import bisect

class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: Total sum
        total_sum = sum(arr)

        # Step 2: LIS using patience sorting (O(n log n))
        tail = []
        dp = [0] * n  # dp[i] = length of LIS ending at index i

        for i in range(n):
            idx = bisect.bisect_left(tail, arr[i])
            if idx == len(tail):
                tail.append(arr[i])
            else:
                tail[idx] = arr[i]
            dp[i] = idx + 1

        # Step 3: Reconstruct the LIS (reverse trace)
        lis_len = max(dp)
        lis = []
        current_len = lis_len
        last_val = float('inf')

        for i in range(n - 1, -1, -1):
            if dp[i] == current_len and arr[i] < last_val:
                lis.append(arr[i])
                last_val = arr[i]
                current_len -= 1

        # Step 4: Subtract LIS sum from total sum
        lis_sum = sum(lis)
        return total_sum - lis_sum
