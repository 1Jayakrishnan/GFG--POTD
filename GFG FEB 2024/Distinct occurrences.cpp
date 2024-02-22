class Solution {
public:
    int subsequenceCount(string s, string t) {
        const int MOD = 1e9 + 7;
        int n = s.length(), m = t.length();

        // Initialize a 2D vector to store the counts
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

        // Initialize the first row with 1 (empty string is a subsequence of any string)
        for (int i = 0; i <= n; ++i) {
            dp[i][0] = 1;
        }

        // Fill the DP array using bottom-up approach
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                // If characters match, consider both characters or ignore the current character in s
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD;
                } else {
                    // If characters do not match, ignore the current character in s
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        // The result is stored in the bottom-right cell of the DP array
        return dp[n][m];
    }
};
