class Solution 
{
     public static void dangeralongside(boolean[][] v,int i,int j,int n,int m) 
     {
         v[i][j]=true;
         if(i+1<n) v[i+1][j]=true;
         if(i-1>=0) v[i-1][j]=true;
         if(j+1<m) v[i][j+1]=true;
         if(j-1>=0) v[i][j-1]=true;
     }
    public static int findShortestPath(int[][] mat) 
    {
        int ans=Integer.MAX_VALUE;
        int n=mat.length;
        int m=mat[0].length;
        boolean v[][]=new boolean[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(mat[i][j]==0)
                dangeralongside(v,i,j,n,m);
            }
        }
        for(int i=0;i<n;i++)
        {
           int min=0;
           if(mat[i][0]!=0&&v[i][0]!=true)
           {
               min=fps(mat,v,i+1,0,n,m,min);
               ans=Math.min(min,ans);  
           }
        }if(ans==Integer.MAX_VALUE) return -1;
        return ans;
    }
     public static int fps(int[][] mat,boolean[][] v,int i,int j,int n,int m,int ans) 
    {
        if(j==m) return ans++;
        if(i<0||i>=n||j<0||j>m||v[i][j]) return Integer.MAX_VALUE;
         v[i][j]=true;
         ans++;
        int r=fps(mat,v,i,j+1,n,m,ans);
        int l=fps(mat,v,i,j-1,n,m,ans);
        int d=fps(mat,v,i+1,j,n,m,ans);
        int u=fps(mat,v,i-1,j,n,m,ans);
        v[i][j]=false;
        r=Math.min(r,l);
        l=Math.min(u,d);
        return ans=Math.min(r,l);
    }
}

