class Solution:
    def compareFrac (self, str):
        # code here
        # Split the string to get both fractions
        fractions = str.split(", ")
        num1 = fractions[0]
        num2 = fractions[1]
        
        a1 = num1.split("/")
        ans1 = int(a1[0])/int(a1[1])
        
        a2 = num2.split("/")
        ans2 = int(a2[0])/int(a2[1])
        
            
        if ans1 == ans2:
            return "equal"
        else:
            if ans1>ans2:
                return num1
            else:
                return num2
