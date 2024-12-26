class Solution {
    boolean twoSum(int arr[], int target) {
        // code here
        HashMap<Integer, Integer> mp = new HashMap<>();
        for(int i=0;i<arr.length;i++){
            int req = target - arr[i];
            if(!mp.containsKey(req)){
                mp.put(arr[i], i);
            }
            else{
                return true;
            }
        }
        return false;
    }
}
