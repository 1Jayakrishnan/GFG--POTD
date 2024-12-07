class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        def merge_and_count(temp_arr, left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to place sorted elements in temp_arr
            inv_count = 0
            
            # Merge the two subarrays
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    # There are (mid - i + 1) inversions because all elements
                    # from arr[i] to arr[mid] are greater than arr[j].
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1
            
            # Copy remaining elements from the left subarray
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1
            
            # Copy remaining elements from the right subarray
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1
            
            # Copy sorted elements back into original array
            for i in range(left, right + 1):
                arr[i] = temp_arr[i]
            
            return inv_count
        
        # Helper function to recursively divide the array and count inversions
        def merge_sort_and_count(temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                
                # Count inversions in the left half
                inv_count += merge_sort_and_count(temp_arr, left, mid)
                
                # Count inversions in the right half
                inv_count += merge_sort_and_count(temp_arr, mid + 1, right)
                
                # Count split inversions while merging
                inv_count += merge_and_count(temp_arr, left, mid, right)
            
            return inv_count
        
        # Initialize temporary array and call the merge sort function
        n = len(arr)
        temp_arr = [0] * n
        return merge_sort_and_count(temp_arr, 0, n - 1)
