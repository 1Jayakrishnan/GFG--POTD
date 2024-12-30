class Solution {
    public static int findUnion(int a[], int b[]) {
        // code here
       HashSet<Integer> union = new HashSet<>();
        for(int x:a)union.add(x);
        
        for(int x:b){
            if(!union.contains(x))union.add(x);
        }
        return union.size();
        
    }
}
