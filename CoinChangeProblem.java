import java.util.Scanner;
public class CoinChangeProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] coins = new int[m];
        for(int i=0; i<m; i++) coins[i] = sc.nextInt();
        long[] dp = new long[n+1];
        dp[0] = 1;
        for(int i=0; i<m; i++){
            for(int j=coins[i]; j<=n; j++){
                dp[j] += dp[j - coins[i]];
            }
        }
        System.out.println(dp[n]);
    }
}
