class solution
{
  public:
      //Function to find the nth catalan number.
      int findCatalan(int n) 
      {
          //code here
          if (n <= 1)
          return 1;
  
          unsigned long long int catalan[n + 1];
          catalan[0] = catalan[1] = 1;
          const int mod = 1e9 + 7;
      
          for (int i = 2; i <= n; i++) {
              catalan[i] = 0;
              for (int j = 0; j < i; j++) {
                  catalan[i] = ((catalan[i] + catalan[j] * catalan[i - j - 1]) % mod) % mod;
              }
          }
      
    return catalan[n];
    }
};
