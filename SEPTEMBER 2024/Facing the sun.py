class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        h = 0
        count = 0
        for i in range(len(height)):
            if height[i] > h:
                count += 1
                h = max(height[i], h)
        
        return count

