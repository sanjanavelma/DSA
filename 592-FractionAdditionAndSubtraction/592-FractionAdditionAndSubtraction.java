// Last updated: 17/06/2025, 22:14:13
class Solution {
    // Helper method to compute the GCD (Greatest Common Divisor) of two numbers
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    // Helper method to add two fractions
    private int[] addFractions(int numerator1, int denominator1, int numerator2, int denominator2) {
        int commonDenominator = denominator1 * denominator2;
        int newNumerator = numerator1 * denominator2 + numerator2 * denominator1;
        
        // Simplify the fraction using GCD
        int gcd = gcd(Math.abs(newNumerator), commonDenominator);
        return new int[]{newNumerator / gcd, commonDenominator / gcd};
    }

    public String fractionAddition(String expression) {
        int numerator = 0, denominator = 1; // Initialize to 0/1

        int i = 0;
        while (i < expression.length()) {
            // Determine the sign of the current fraction
            int sign = 1;
            if (expression.charAt(i) == '-' || expression.charAt(i) == '+') {
                sign = expression.charAt(i) == '-' ? -1 : 1;
                i++;
            }
            
            // Parse the numerator
            int start = i;
            while (i < expression.length() && Character.isDigit(expression.charAt(i))) {
                i++;
            }
            int num = Integer.parseInt(expression.substring(start, i)) * sign;

            // Skip the '/'
            i++;
            
            // Parse the denominator
            start = i;
            while (i < expression.length() && Character.isDigit(expression.charAt(i))) {
                i++;
            }
            int denom = Integer.parseInt(expression.substring(start, i));

            // Add the current fraction to the accumulated result
            int[] result = addFractions(numerator, denominator, num, denom);
            numerator = result[0];
            denominator = result[1];
        }

        // Return the final result in the format "numerator/denominator"
        return numerator + "/" + denominator;
    }
}
