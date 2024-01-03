class Solution:
    def smallestSubstring(self, S):
        # Code here
        count_0 = count_1 = count_2 = 0

        # Create a dictionary to track the counts of each character in the window
        char_counts = {'0': 0, '1': 0, '2': 0}

        # Initialize pointers for the sliding window
        left_pointer = 0
        min_length = float('inf')  # Initialize with positive infinity

        # Iterate over the string using the right pointer
        for right_pointer in range(len(S)):
            # Update the count and character dictionary for the current character
            char_counts[S[right_pointer]] += 1

            # Update the individual counts
            if S[right_pointer] == '0':
                count_0 += 1
            elif S[right_pointer] == '1':
                count_1 += 1
            elif S[right_pointer] == '2':
                count_2 += 1

            # Check if the current window contains all three characters
            while count_0 > 0 and count_1 > 0 and count_2 > 0:
                # Update the minimum length
                min_length = min(min_length, right_pointer - left_pointer + 1)

                # Move the left pointer to the right to shrink the window
                char_counts[S[left_pointer]] -= 1
                if S[left_pointer] == '0':
                    count_0 -= 1
                elif S[left_pointer] == '1':
                    count_1 -= 1
                elif S[left_pointer] == '2':
                    count_2 -= 1

                left_pointer += 1

        # If min_length is still positive infinity, no valid substring was found
        return -1 if min_length == float('inf') else min_length
