class Solution:
    def splitArray(self, arr, k):
        def isValid(maxSum):
            count = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > maxSum:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            return True

        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
