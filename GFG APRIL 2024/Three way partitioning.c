void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void threeWayPartition(int arr[], int n, int a, int b) {
    int low = 0, mid = 0, high = n - 1;
    
    while (mid <= high) {
        if (arr[mid] < a) {
            swap(&arr[low], &arr[mid]);
            low++;
            mid++;
        }
        else if (arr[mid] > b) {
            swap(&arr[mid], &arr[high]);
            high--;
        }
        else {
            mid++;
        }
    }
}
