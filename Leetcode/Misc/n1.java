// https://leetcode.com/problems/powx-n/description/

public class n1 {
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        
        double result = 1;
        double current_product = x;
        
        for (long i = N; i > 0; i /= 2) {
            if (i % 2 == 1) {
                result *= current_product;
            }
            current_product *= current_product;
        }
        
        return result;
    }
}