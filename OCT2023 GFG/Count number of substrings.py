class Solution:
    def substrCount (self,s, k):
        # your code here
        def atMostKDistinct(s, k):
            count = [0] * 26  # Assuming the input only contains lowercase alphabets
            left = 0
            distinct_count = 0
            substr_count = 0

            for right in range(len(s)):
                if count[ord(s[right]) - ord('a')] == 0:
                    distinct_count += 1
                count[ord(s[right]) - ord('a')] += 1

                while distinct_count > k:
                    count[ord(s[left]) - ord('a')] -= 1
                    if count[ord(s[left]) - ord('a')] == 0:
                        distinct_count -= 1
                    left += 1

                substr_count += right - left + 1

            return substr_count

        return atMostKDistinct(s, k) - atMostKDistinct(s, k - 1)
