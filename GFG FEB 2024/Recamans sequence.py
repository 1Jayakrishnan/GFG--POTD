class Solution:
    def recamanSequence(self, n):
        # code here
        if n <= 0:
            return []

        sequence = [0]
        seen_set = {0}

        for i in range(1, n):
            prev_term = sequence[-1]
            next_term = prev_term - i

            if next_term < 0 or next_term in seen_set:
                next_term = prev_term + i

            sequence.append(next_term)
            seen_set.add(next_term)

        return sequence
