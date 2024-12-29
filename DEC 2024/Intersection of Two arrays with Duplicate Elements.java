class Solution {
    public ArrayList<Integer> intersectionWithDuplicates(int[] a, int[] b) {
        // code here
        HashSet<Integer> set1 = new HashSet<>();
        for(int x:a)set1.add(x);
        
        HashSet<Integer> Int = new HashSet<>();
        for(int x:b){
            if(set1.contains(x)){
                Int.add(x);
            }
        }
        return new ArrayList(Int);
    }
}
