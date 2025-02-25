class Solution:
    def getMaxArea(self,arr):
        #code here
        n = len(arr)
        stack = []
        max_area = 0
        index = 0
        
        # Process all bars of the histogram
        while index < n:
            # If stack is empty or current bar is higher than the bar at stack top, push index.
            if not stack or arr[index] >= arr[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Pop the top element and calculate the area with arr[top] as the smallest bar.
                top = stack.pop()
                if not stack:
                    area = arr[top] * index
                else:
                    area = arr[top] * (index - stack[-1] - 1)
                max_area = max(max_area, area)
        
        # Process remaining bars in stack
        while stack:
            top = stack.pop()
            if not stack:
                area = arr[top] * index
            else:
                area = arr[top] * (index - stack[-1] - 1)
            max_area = max(max_area, area)
        
        return max_area
