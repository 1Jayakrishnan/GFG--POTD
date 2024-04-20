class Solution
{
    //Function to return a list containing the union of the two arrays.
    public static ArrayList<Integer> findUnion(int arr1[], int arr2[], int n, int m)
    {
        HashSet<Integer> set = new HashSet<>();
        
        for(int i=0; i<n || i<m; i++){
            if(i<n){
                set.add(arr1[i]);
            }
            
            if(i<m){
                set.add(arr2[i]);
            }
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i : set){
            list.add(i);
        }
        Collections.sort(list);
        return list;
    }
}
