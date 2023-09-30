void booleanMatrix(int R, int C, int matrix[][C])
{
    // Arrays to keep track of rows and columns to be updated
    int row[R];
    int col[C];

    // Initialize row and col arrays
    for (int i = 0; i < R; i++) {
        row[i] = 0;
    }
    for (int j = 0; j < C; j++) {
        col[j] = 0;
    }

    // Find the rows and columns to be updated
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (matrix[i][j] == 1) {
                row[i] = 1;
                col[j] = 1;
            }
        }
    }

    // Update the matrix based on the row and column arrays
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (row[i] == 1 || col[j] == 1) {
                matrix[i][j] = 1;
            }
        }
    }
}
