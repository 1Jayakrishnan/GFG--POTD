
class Solution {
    public static ArrayList<ArrayList<Integer>> kTop(int[] arr, int N, int K) {
        // code here
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        // PriorityQueue to store elements based on frequency
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
            (a, b) -> a.getValue() != b.getValue() ? b.getValue() - a.getValue() : a.getKey() - b.getKey()
        );

        for (int i = 0; i < N; i++) {
            // Update frequency map
            frequencyMap.put(arr[i], frequencyMap.getOrDefault(arr[i], 0) + 1);

            // Add entries to the PriorityQueue
            pq.clear();
            pq.addAll(frequencyMap.entrySet());

            // Create an array for the current iteration
            ArrayList<Integer> currentIteration = new ArrayList<>();

            // Add top K elements to the array
            int count = 0;
            while (!pq.isEmpty() && count < K) {
                currentIteration.add(pq.poll().getKey());
                count++;
            }

            // Add the array to the result
            result.add(currentIteration);
        }

        return result;
    }
}
      
