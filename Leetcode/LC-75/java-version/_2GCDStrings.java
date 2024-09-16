// https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
// COMPLETE

import java.util.*;

public class _2GCDStrings {
    private static boolean checkDivides(String s, String t) {
        int repeatCount = s.length() / t.length();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < repeatCount; i++) {
            sb.append(t);
        }
        return s.equals(sb.toString());
    }

    public static String gcdOfStrings(String str1, String str2) {
        int gcdLength = gcd(str1.length(), str2.length());
        
        String candidate = str1.substring(0, gcdLength);
        
        if (checkDivides(str1, candidate) && checkDivides(str2, candidate)) {
            return candidate;
        } else {
            return "";
        }
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
