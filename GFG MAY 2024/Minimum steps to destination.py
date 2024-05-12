class Solution:
    def minSteps(self, d):
        # code here
        d=abs(d)
        steps=0
        sm=0
        while sm<d or abs(sm-d)%2!=0:
            steps+=1
            sm+=steps

        return steps
