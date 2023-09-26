#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        n = len(arr)
        out = []

        arr.sort()

        for q1 in range(n):
            if q1 > 0 and arr[q1] == arr[q1 - 1]:
                continue

            for q2 in range(q1 + 1, n):
                if q2 > q1 + 1 and arr[q2] == arr[q2 - 1]:
                    continue

                q3, q4 = q2 + 1, n - 1

                while q3 < q4:
                    _sum = arr[q1] + arr[q2] + arr[q3] + arr[q4]

                    if _sum == k:
                        out.append([arr[q1], arr[q2], arr[q3], arr[q4]])
                        q3 += 1
                        q4 -= 1

                        while q3 < q4 and arr[q3] == arr[q3 - 1]:
                            q3 += 1
                        while q3 < q4 and arr[q4] == arr[q4 + 1]:
                            q4 -= 1
                    elif _sum < k:
                        q3 += 1
                    else:
                        q4 -= 1

        return out
