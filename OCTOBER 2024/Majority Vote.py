class Solution:
    def findMajority(self, nums):
        # Edge case: If nums is empty, return [-1]
        if not nums:
            return [-1]
        
        # Step 1: Find the potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Validate the candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 3: Prepare the result
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        # If no candidate found, return [-1]
        if not result:
            return [-1]
        
        return result
