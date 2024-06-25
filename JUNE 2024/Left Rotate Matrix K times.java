class Solution {
    int[][] rotateMatrix(int k, int mat[][]) {
        // code here
        int rows = mat.length;
        int cols = mat[0].length;
        
        k = k % cols;  // Effective rotation
        
        int[][] result = new int[rows][cols];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][(j + cols - k) % cols] = mat[i][j];
            }
        }
        
        return result;
    }
}
