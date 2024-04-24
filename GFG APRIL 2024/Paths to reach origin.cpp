class Solution
{
public:
    int dp[1001][1001];
    int mod = 1e9 + 7;
    int ncr(int n, int r){
        if(r == 0 ||  n == r) return 1;
        if( r == 1) return n;
        if(dp[n][r] != -1) return dp[n][r];
        return dp[n][r] = (ncr(n-1, r) + ncr(n -1, r -1))%mod;
        
    }
    int ways(int x, int y)
    {
        memset(dp, -1, sizeof(dp));
       return ncr(x + y, x);
    }
};
