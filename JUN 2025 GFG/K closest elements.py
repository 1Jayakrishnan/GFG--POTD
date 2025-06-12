import bisect

class Solution:
    def printKClosest(self, arr, k, x):
        n = len(arr)
        index = bisect.bisect_left(arr, x)

        left = index - 1
        right = index if index == n or arr[index] != x else index + 1

        result = []

        while k > 0:
            if left >= 0 and right < n:
                left_diff = abs(arr[left] - x)
                right_diff = abs(arr[right] - x)
                if left_diff < right_diff:
                    result.append(arr[left])
                    left -= 1
                elif left_diff > right_diff:
                    result.append(arr[right])
                    right += 1
                else:
                    if arr[left] > arr[right]:
                        result.append(arr[left])
                        left -= 1
                    else:
                        result.append(arr[right])
                        right += 1
            elif left >= 0:
                result.append(arr[left])
                left -= 1
            elif right < n:
                result.append(arr[right])
                right += 1
            else:
                break
            k -= 1

        return result
