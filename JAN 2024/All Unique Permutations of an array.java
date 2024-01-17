class Solution {
    static ArrayList<ArrayList<Integer>> uniquePerms(ArrayList<Integer> arr, int n) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        ArrayList<Integer> currentPerm = new ArrayList<>();
        boolean[] used = new boolean[n];

        // Sort the array to ensure permutations are in sorted order
        Collections.sort(arr);

        generatePermutations(arr, n, currentPerm, used, result);

        return result;
    }

    static void generatePermutations(ArrayList<Integer> arr, int n, ArrayList<Integer> currentPerm, boolean[] used, ArrayList<ArrayList<Integer>> result) {
        if (currentPerm.size() == n) {
            result.add(new ArrayList<>(currentPerm));
            return;
        }

        for (int i = 0; i < n; i++) {
            // Skip used elements to avoid duplicates
            if (used[i]) continue;

            // Skip duplicates to ensure sorted order
            if (i > 0 && arr.get(i).equals(arr.get(i - 1)) && !used[i - 1]) continue;

            used[i] = true;
            currentPerm.add(arr.get(i));

            generatePermutations(arr, n, currentPerm, used, result);

            used[i] = false;
            currentPerm.remove(currentPerm.size() - 1);
        }
    }
}
