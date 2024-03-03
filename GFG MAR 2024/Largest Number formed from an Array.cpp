bool customCompare(const string &a, const string &b) {
    // Concatenate two strings in different orders and compare the results
    string order1 = a + b;
    string order2 = b + a;
    return order1 > order2;
}

class Solution {
public:
    string printLargest(int n, vector<string> &arr) {
        // Sort the array of strings using the custom comparison function
        sort(arr.begin(), arr.end(), customCompare);

        // Concatenate the sorted strings to get the largest possible number
        string result;
        for (const string &s : arr) {
            result += s;
        }

        return result;
    }
};
