class Solution:
    def InternalCount(self, p, q, r):
        
        def area(p, q, r):
            return abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))

        def boundary_points(p, q):
            return math.gcd(abs(p[0] - q[0]), abs(p[1] - q[1]))

        # Compute the twice of area (since it's easier to work with integers)
        A2 = area(p, q, r)

        # Compute boundary points
        B = boundary_points(p, q) + boundary_points(q, r) + boundary_points(r, p)

        # Apply Pick's theorem on twice the area
        I = (A2 - B + 2) // 2
        
        return I
