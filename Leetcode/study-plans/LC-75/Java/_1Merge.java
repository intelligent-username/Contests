// https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
// COMPLETE
// Make it more efficient later rn quick testing LeetCode

public class _1Merge {
    public static String main(String word1, String word2) {
        StringBuilder combined = new StringBuilder();
        int l1 = word1.length();
        int l2 = word2.length();
        int minLength = Math.min(l1, l2);

        // Merge alternately up to the length of the shorter string
        for (int i = 0; i < minLength; i++) {
            combined.append(word1.charAt(i));
            combined.append(word2.charAt(i));
        }

        // Append the remainder of the longer string
        if (l1 > l2) {
            combined.append(word1.substring(l2));
        } else if (l2 > l1) {
            combined.append(word2.substring(l1));
        }

        return combined.toString();
    }
}
