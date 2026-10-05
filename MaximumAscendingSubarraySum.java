import java.util.Scanner;
public class MaximumAscendingSubarraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long max = 0, sum = 0;
        long prev = -1;
        for(int i=0; i<n; i++){
            long curr = sc.nextLong();
            if(curr > prev){
                sum += curr;
            } else {
                sum = curr;
            }
            if(sum > max) max = sum;
            prev = curr;
        }
        System.out.println(max);
    }
}
