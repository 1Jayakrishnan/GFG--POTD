from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        n = len(arr)
        if n % k != 0:
            return False

        count = Counter(arr)
        keys = sorted(count.keys())

        for num in keys:
            if count[num] > 0:
                freq = count[num]
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False
                    count[i] -= freq
        return True
