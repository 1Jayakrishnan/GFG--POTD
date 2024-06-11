from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Create a list of orders with their tips and the difference between tips
        orders = []
        for i in range(n):
            orders.append((arr[i], brr[i], abs(arr[i] - brr[i])))
        
        # Sort the orders based on the difference in descending order
        orders.sort(key=lambda x: x[2], reverse=True)
        
        total_tips = 0
        a_count = 0
        b_count = 0
        
        # Distribute the orders based on the sorted differences
        for a_tip, b_tip, _ in orders:
            if (a_tip >= b_tip and a_count < x) or b_count >= y:
                total_tips += a_tip
                a_count += 1
            else:
                total_tips += b_tip
                b_count += 1
        
        return total_tips
