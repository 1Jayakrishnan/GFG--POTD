void rotateby90(int n, int mat[][n]) {
    // code here
    // Step 1: Transpose the matrix
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int temp = mat[i][j];
            mat[i][j] = mat[j][i];
            mat[j][i] = temp;
        }
    }
    
    // Step 2: Reverse each column
    for (int j = 0; j < n; j++) {
        for (int i = 0, k = n - 1; i < k; i++, k--) {
            int temp = mat[i][j];
            mat[i][j] = mat[k][j];
            mat[k][j] = temp;
        }
    }
}
