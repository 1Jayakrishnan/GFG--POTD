class Solution
{
    public:
    //Function to check if two strings are isomorphic.
    bool areIsomorphic(string str1, string str2)
    {
        
        // Your code here
        if (str1.length() != str2.length()) {
            return false;
        }

        unordered_map<char, char> charMap;  // Map to store the mapping between characters.

        for (int i = 0; i < str1.length(); ++i) {
            char ch1 = str1[i];
            char ch2 = str2[i];

            // If ch1 is already mapped, it should map to ch2.
            if (charMap.find(ch1) != charMap.end()) {
                if (charMap[ch1] != ch2) {
                    return false;  // Inconsistent mapping.
                }
            } else {
                // If ch1 is not mapped, but ch2 is already mapped to some other character, it's not isomorphic.
                for (const auto& pair : charMap) {
                    if (pair.second == ch2) {
                        return false;  // Inconsistent mapping.
                    }
                }
                charMap[ch1] = ch2;  // Add the mapping.
            }
        }

        return true;
        
    }
};
