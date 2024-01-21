class Solution {
public:
    void solve(int i, int bits, int n, int m, vector<pair<int, int>>& edges, int &out) {
        if (i > n) {
            for (int i = 0; i < m; i++) {
                if (!((1 << (edges[i].first - 1) & bits) != 0 || (1 << (edges[i].second - 1) & bits) != 0)) {
                    return;
                }
            }
            out = min(out, __builtin_popcount(bits));
            return;
        }
        solve(i + 1, bits, n, m, edges, out);
        solve(i + 1, bits | 1 << (i - 1), n, m, edges, out);
    }

    int vertexCover(int n, vector<pair<int, int>> &edges) {
        int out = INT_MAX;
        int m = edges.size();
        solve(1, 0, n, m, edges, out);
        return out;
    }
};
