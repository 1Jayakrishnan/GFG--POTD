class Solution
{
private:
    bool solve_rec(string s, unordered_set<string>& st, int index) {
        if(index == s.size()) return 1;

        for(int i = index; i < s.size(); i++) {
            if(st.count(s.substr(index, i+1-index)) && solve_rec(s, st, i+1)) {
                return 1;
            }
        }
        return 0;
    }

    bool solveMem(string s, unordered_set<string>& st, int index, vector<int>& dp) {
        if(index == s.size()) return 1;

        if(dp[index] != -1) return dp[index];

        for(int i = index; i < s.size(); i++) {
            if(st.count(s.substr(index, i+1-index)) && solveMem(s, st, i+1, dp)) {
                return 1;
            }
        }
        return dp[index] = 0;
    }

    bool solveTab(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<int> dp(n+1, 0);

        dp[0] = 1;
                
        unordered_set<string> st;
        for(auto i : wordDict) st.insert(i);
        
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j < i; j++) {
                if(dp[j] && st.count(s.substr(j, i-j))) {
                    dp[i] = 1;
                    break;
                }
            }
        }
        return dp[n];
    }
public:
    int wordBreak(int n, string A, vector<string> &B) {
        unordered_set<string> st;
        
        for (auto& str : B) st.insert(str);
        
        return solveTab(A, B);
    }
};
