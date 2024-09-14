class Solution:
    def rearrange(self,arr):
        # code here
        pos = [num for num in arr if num>=0]
        neg = [num for num in arr if num<0]
        # print(pos)
        # print(neg)
        if len(pos) < len(neg):
            small = len(pos)
        else:
            small = len(neg)
            
        new_arr = []
        
        for i in range(small):
            new_arr.append(pos[i])
            new_arr.append(neg[i])
            
        #remaining numbers
        if len(pos) > small:
            new_arr.extend(pos[small:])
        
        if len(neg) > small:
            new_arr.extend(neg[small:])
                
        #print(new_arr)
        # Update the original arr in place
        for i in range(len(arr)):
            arr[i] = new_arr[i]
        
        return arr
