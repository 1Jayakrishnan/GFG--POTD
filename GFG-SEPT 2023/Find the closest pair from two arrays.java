class Solution{
    // Function for finding maximum and value pair
    public static ArrayList<Integer> printClosest (int arr[], int brr[], int n, int m, int x) {
        // code here
        // Initialize variables to store the result
        ArrayList<Integer> result = new ArrayList<>();
        int minDiff = Integer.MAX_VALUE;
        int left = 0, right = m - 1;

        // Traverse both arrays from left and right
        while (left < n && right >= 0) {
            int sum = arr[left] + brr[right];
            int diff = Math.abs(sum - x);

            // If the current pair has a smaller difference, update the result
            if (diff < minDiff) {
                minDiff = diff;
                result.clear();
                result.add(arr[left]);
                result.add(brr[right]);
            }

            // If the sum is less than x, increment the left pointer
            if (sum < x) {
                left++;
            }
            // If the sum is greater than or equal to x, decrement the right pointer
            else {
                right--;
            }
        }
        return result;
    }
}
