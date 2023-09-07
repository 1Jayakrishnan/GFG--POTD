from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0

        n = len(arr)
        visited = set()
        queue = [(start, 0)]

        while queue:
            current, steps = queue.pop(0)

            for num in arr:
                new_start = (current * num) % 100000

                if new_start == end:
                    return steps + 1

                if new_start not in visited:
                    visited.add(new_start)
                    queue.append((new_start, steps + 1))

        return -1
