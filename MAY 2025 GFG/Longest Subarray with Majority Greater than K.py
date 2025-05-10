#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        
        # Step 1: Convert the array into +1 and -1
        mapped = [1 if x > k else -1 for x in arr]

        prefix_sum = 0
        max_len = 0
        seen = {}  # Hash map to store first occurrence of each prefix sum

        for i in range(n):
            prefix_sum += mapped[i]

            # Case 1: If current prefix sum > 0, entire subarray from 0 to i is valid
            if prefix_sum > 0:
                max_len = i + 1

            # Case 2: Check if (prefix_sum - 1) was seen before
            # That means there is a subarray with net +1 more 1s than -1s
            if (prefix_sum - 1) in seen:
                max_len = max(max_len, i - seen[prefix_sum - 1])

            # Store the first occurrence of the prefix sum
            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return max_len



#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends
