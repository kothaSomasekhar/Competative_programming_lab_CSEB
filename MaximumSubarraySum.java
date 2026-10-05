import java.util.Scanner;
public class MaximumSubarraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextInt()){
            int n = sc.nextInt();
            long max = Long.MIN_VALUE, sum = 0;
            for(int i=0; i<n; i++){
                long val = sc.nextLong();
                sum += val;
                if(sum > max) max = sum;
                if(sum < 0) sum = 0;
            }
            System.out.println(max);
        }
    }
}
