class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def isPossible(target):
            operations = [0] * (n + 1)
            ops_used = 0
            water = 0
            
            for i in range(n):
                water += operations[i]
                current_height = arr[i] + water

                if current_height < target:
                    need = target - current_height
                    ops_used += need
                    if ops_used > k:
                        return False
                    water += need
                    if i + w < len(operations):
                        operations[i + w] -= need
                    
            return True

        low = min(arr)
        high = low + k
        result = low

        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
