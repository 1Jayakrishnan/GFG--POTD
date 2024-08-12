class Solution {
    // Function to find the maximum profit and the number of jobs done.
    int[] JobScheduling(Job arr[], int n) {
        // Step 1: Sort jobs by profit in descending order
        Arrays.sort(arr, new Comparator<Job>() {
            public int compare(Job a, Job b) {
                return b.profit - a.profit;
            }
        });

        // Step 2: Find the maximum deadline
        int maxDeadline = 0;
        for (Job job : arr) {
            if (job.deadline > maxDeadline) {
                maxDeadline = job.deadline;
            }
        }

        // Step 3: Initialize slots to keep track of free time slots
        int[] slots = new int[maxDeadline + 1];  // +1 because slot indexing starts from 1
        Arrays.fill(slots, -1);  // Initialize all slots to -1 (indicating empty)

        // Initialize count of jobs done and total profit
        int count = 0;
        int totalProfit = 0;

        // Step 4: Allocate jobs to slots
        for (Job job : arr) {
            // Find a free slot for this job from its deadline moving backward
            for (int slot = job.deadline; slot > 0; slot--) {
                if (slots[slot] == -1) {
                    slots[slot] = job.id;
                    count++;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        // Return the result as an array: [number of jobs done, total profit]
        return new int[]{count, totalProfit};
    }
}
