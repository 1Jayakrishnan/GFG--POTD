class Solution {
    public ArrayList<ArrayList<String>> anagrams(String[] arr) {
        // code here
        // Map to store grouped anagrams
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        for(String word : arr){
             // Sort the characters of the word to create a key
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sorted_word = new String(charArray);
             // Add the word to the respective group in the map
            if(!map.containsKey(sorted_word)){
                map.put(sorted_word, new ArrayList<>());
            }
            map.get(sorted_word).add(word);
        }
        // Convert the map values to an ArrayList of ArrayLists
        return new ArrayList<>(map.values());
    }
}
