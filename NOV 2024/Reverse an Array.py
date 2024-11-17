class Solution:
    def reverseArray(self, arr):
        # code here
        l = len(arr)-1
        for i in range((l//2)+1):
            arr[i], arr[l-i] = arr[l-i], arr[i]
