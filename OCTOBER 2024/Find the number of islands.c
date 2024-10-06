void dfs(int M[][COL], int x, int y, int n, int m) {
    // Check for boundary conditions
    if (x < 0 || y < 0 || x >= n || y >= m || M[x][y] == 0)
        return;
    
    // Mark the current cell as visited
    M[x][y] = 0;
    
    // Arrays to explore all 8 directions (up, down, left, right, and diagonals)
    int row_dir[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int col_dir[] = {-1, 0, 1, -1, 1, -1, 0, 1};
    
    // Explore all 8 possible directions
    for (int i = 0; i < 8; i++) {
        int new_x = x + row_dir[i];
        int new_y = y + col_dir[i];
        dfs(M, new_x, new_y, n, m);
    }
}

// Function to count the number of islands
int numIslands(int M[][COL], int n, int m) {
    int count = 0;  // To store the number of islands

    // Traverse the grid
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // If a land cell is found
            if (M[i][j] == 1) {
                // Start a DFS to mark the whole island
                dfs(M, i, j, n, m);
                count++;  // Increment island count
            }
        }
    }

    return count;  // Return the number of islands
}
