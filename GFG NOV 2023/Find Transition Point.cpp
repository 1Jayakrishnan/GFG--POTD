class Solution
{
public:    
    int transitionPoint(int arr[], int n) {
        int l = 0, r = n - 1;
        while (l < r) {
            int m = (l + r) / 2;
            
            if (arr[m] < 1)
                l = m + 1;
            else
                r = m;
        }
        
        return arr[l] ? l : -1;
    }
};
