class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int write = 0, read = 0;
        
        while (read < n) {
            char currentChar = chars[read];
            int count = 0;
            
            // Count occurrences of the current character
            while (read < n && chars[read] == currentChar) {
                read++;
                count++;
            }
            
            // Write the current character
            chars[write++] = currentChar;
            
            // If the count is greater than 1, write the number
            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[write++] = c;
                }
            }
        }
        
        return write; // The length of the compressed string
    }
};
