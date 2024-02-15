class Solution {
    public int isPossible(int[][] paths) {
        int n = paths.length;

        // Check if the graph is connected
        if (!isConnected(paths, n)) {
            return 0;
        }

        // Check if all vertices have even degree
        for (int i = 0; i < n; i++) {
            int degree = 0;
            for (int j = 0; j < n; j++) {
                degree += paths[i][j];
            }
            if (degree % 2 != 0) {
                return 0;
            }
        }

        return 1;
    }

    private boolean isConnected(int[][] paths, int n) {
        boolean[] visited = new boolean[n];
        dfs(paths, 0, visited);

        for (boolean vertexVisited : visited) {
            if (!vertexVisited) {
                return false; // Not all vertices are reachable
            }
        }

        return true;
    }

    private void dfs(int[][] paths, int node, boolean[] visited) {
        visited[node] = true;

        for (int i = 0; i < paths.length; i++) {
            if (paths[node][i] == 1 && !visited[i]) {
                dfs(paths, i, visited);
            }
        }
    }
}
