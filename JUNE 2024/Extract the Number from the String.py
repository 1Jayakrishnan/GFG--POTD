class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l = sentence.split(" ")
        arr = []
        for i in l:
            arr.append(i)
            
        numbers = []
        for num in arr:
            if num.isdigit() and '9' not in str(num):
                numbers.append(int(num))
                
        new_list = sorted(numbers)
        
        if new_list == []:
            return -1
        else:
            return new_list[-1]
