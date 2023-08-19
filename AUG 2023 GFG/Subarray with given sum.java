class Solution
{
    //Function to find a continuous sub-array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) 
    {
        // Your code here
       ArrayList<Integer> res = new ArrayList<Integer>();
       if(s == 0)
       {
           res.add(-1);
           return res;
       }
       int start = 0,end = 0,sum = 0;
       while(end < n)
       {
           if(sum + arr[end] <= s){
               sum += arr[end++];
           }else{
               sum -= arr[start++];
           }
           
           if(sum == s){
               res.add(start+1);
               res.add(end);
               return res;
           }
       }
       res.add(-1);
       return res;
    }
}
