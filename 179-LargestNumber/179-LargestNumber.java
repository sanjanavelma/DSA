// Last updated: 17/06/2025, 22:14:23
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String largestNumber(int[] nums) {
        // Convert the integers to strings
        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }
        
        // Sort the array using a custom comparator
        Arrays.sort(strNums, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                // Compare concatenated results (a+b vs b+a)
                return (b + a).compareTo(a + b);
            }
        });
        
        // Edge case: if the largest number is 0, return "0"
        if (strNums[0].equals("0")) {
            return "0";
        }
        
        // Join the sorted array into a single string
        StringBuilder largestNumber = new StringBuilder();
        for (String num : strNums) {
            largestNumber.append(num);
        }
        
        return largestNumber.toString();
    }
}
