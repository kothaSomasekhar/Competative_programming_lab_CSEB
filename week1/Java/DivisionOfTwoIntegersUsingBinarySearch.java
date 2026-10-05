import java.util.Scanner;
public class DivisionOfTwoIntegersUsingBinarySearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextLong()) return;
        long dividend = sc.nextLong();
        long divisor = sc.nextLong();
        boolean neg = (dividend < 0) ^ (divisor < 0);
        long num = Math.abs(dividend);
        long den = Math.abs(divisor);
        long low = 0, high = num, ans = 0;
        while(low <= high){
            long mid = low + (high - low) / 2;
            if(mid * den <= num){
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        System.out.println(neg ? -ans : ans);
    }
}
