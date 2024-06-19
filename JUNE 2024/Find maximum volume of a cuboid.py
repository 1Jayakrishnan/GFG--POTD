import math
class Solution:
    def maxVolume(self, perimeter, area):
        #code here
        l = (perimeter-math.sqrt((perimeter*perimeter)-(24*area)))/12
        v = ((l*area)/2)-(((l*l)*perimeter)/4)+(l*l*l)
        return round(v,2)
