import java.util.Scanner;
public class WildCardPatterns {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String str = sc.nextLine();
            String pat = sc.nextLine();
            int n = str.length(), m = pat.length();
            boolean[][] dp = new boolean[n+1][m+1];
            dp[0][0] = true;
            for(int j=1; j<=m; j++){
                if(pat.charAt(j-1) == '*') dp[0][j] = dp[0][j-1];
            }
            for(int i=1; i<=n; i++){
                for(int j=1; j<=m; j++){
                    if(pat.charAt(j-1) == '*') dp[i][j] = dp[i-1][j] || dp[i][j-1];
                    else if(pat.charAt(j-1) == '?' || str.charAt(i-1) == pat.charAt(j-1))
                        dp[i][j] = dp[i-1][j-1];
                }
            }
            System.out.println(dp[n][m] ? "TRUE" : "FALSE");
        }
    }
}
