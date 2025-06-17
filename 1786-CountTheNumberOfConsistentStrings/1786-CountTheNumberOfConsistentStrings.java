// Last updated: 17/06/2025, 22:13:46
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        // Step 1: Create a set of allowed characters
        Set<Character> allowedSet = new HashSet<>();
        for (char ch : allowed.toCharArray()) {
            allowedSet.add(ch);
        }
        
        // Step 2: Initialize a counter for consistent strings
        int count = 0;
        
        // Step 3: Check each word
        for (String word : words) {
            boolean isConsistent = true;
            for (char ch : word.toCharArray()) {
                if (!allowedSet.contains(ch)) {
                    isConsistent = false;
                    break;
                }
            }
            if (isConsistent) {
                count++;
            }
        }
        
        // Step 4: Return the total count of consistent strings
        return count;
    }
}
