class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        # Helper function to find the orientation of the ordered triplet (p, q, r)
        # 0 -> p, q, and r are collinear
        # 1 -> Clockwise
        # 2 -> Counterclockwise
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        # Helper function to check if point q lies on segment pr
        def onSegment(p, q, r):
            if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
                return True
            return False

        # Find the four orientations needed for the general and special cases
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        # General case
        if o1 != o2 and o3 != o4:
            return "true"

        # Special cases
        # p1, q1, and p2 are collinear and p2 lies on segment p1q1
        if o1 == 0 and onSegment(p1, p2, q1):
            return "true"

        # p1, q1, and q2 are collinear and q2 lies on segment p1q1
        if o2 == 0 and onSegment(p1, q2, q1):
            return "true"

        # p2, q2, and p1 are collinear and p1 lies on segment p2q2
        if o3 == 0 and onSegment(p2, p1, q2):
            return "true"

        # p2, q2, and q1 are collinear and q1 lies on segment p2q2
        if o4 == 0 and onSegment(p2, q1, q2):
            return "true"

        # If none of the cases apply, the segments do not intersect
        return "false"
