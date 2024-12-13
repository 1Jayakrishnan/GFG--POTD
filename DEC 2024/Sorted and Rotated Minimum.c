int findMin(int* arr, int n) {
    // code here
    int low = 0, high = n - 1;

    while (low < high) {
        int mid = low + (high - low) / 2;

        // Check if mid is the minimum
        if (arr[mid] > arr[high]) {
            // Minimum is in the right half
            low = mid + 1;
        } else if (arr[mid] < arr[high]) {
            // Minimum is in the left half (or is mid)
            high = mid;
        } else {
            // When arr[mid] == arr[high], reduce the search space
            high--;
        }
    }
    // `low` now points to the minimum element
    return arr[low];
    
}
