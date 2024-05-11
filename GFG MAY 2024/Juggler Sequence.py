class Solution:
    def jugglerSequence(self, n):
        seq = [n]
        while seq[-1] != 1:
            # seq.append(n)
            if seq[-1]&1:
                seq.append(int(seq[-1]**(3/2)))
            else:
                # n = int(n**(3/2))
                seq.append(int(seq[-1]**(1/2)))
        return seq
