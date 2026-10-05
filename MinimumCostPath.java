import java.util.Scanner;
public class MinimumCostPath {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[][] cost = new int[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++) cost[i][j] = sc.nextInt();
        }
        int[][] tc = new int[m][n];
        tc[0][0] = cost[0][0];
        for(int i=1; i<m; i++) tc[i][0] = tc[i-1][0] + cost[i][0];
        for(int j=1; j<n; j++) tc[0][j] = tc[0][j-1] + cost[0][j];
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                tc[i][j] = cost[i][j] + Math.min(tc[i-1][j-1], Math.min(tc[i-1][j], tc[i][j-1]));
            }
        }
        System.out.println(tc[m-1][n-1]);
    }
}
