class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        seen_rows = set()
        repeated_rows = []

        for i in range(m):
            row_as_string = ''.join(map(str, arr[i]))
            
            # Check if the row is already in the set
            if row_as_string in seen_rows:
                repeated_rows.append(i)
            else:
                seen_rows.add(row_as_string)

        return repeated_rows
