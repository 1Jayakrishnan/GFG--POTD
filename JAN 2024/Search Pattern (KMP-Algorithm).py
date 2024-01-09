class Solution:
    def search(self, pat, txt):
        def build_prefix_array(pattern):
            prefix_array = [0] * len(pattern)
            j = 0

            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = prefix_array[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                prefix_array[i] = j

            return prefix_array

        indices = []
        pat_length = len(pat)
        txt_length = len(txt)
        prefix_array = build_prefix_array(pat)

        j = 0
        for i in range(txt_length):
            while j > 0 and txt[i] != pat[j]:
                j = prefix_array[j - 1]

            if txt[i] == pat[j]:
                j += 1

            if j == pat_length:
                indices.append(i - j + 2)
                j = prefix_array[j - 1]

        return indices
