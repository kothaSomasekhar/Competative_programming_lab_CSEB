import os

problems = {
    "CalculateLengthOfString": """import java.util.Scanner;
public class CalculateLengthOfString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            System.out.println(s.length());
        }
    }
}
""",
    "InterchangingNumbersInArray": """import java.util.Scanner;
public class InterchangingNumbersInArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextInt()){
            int n = sc.nextInt();
            int[] arr = new int[n];
            for(int i=0; i<n; i++) arr[i] = sc.nextInt();
            if(n >= 2){
                int temp = arr[0];
                arr[0] = arr[n-1];
                arr[n-1] = temp;
            }
            for(int i=0; i<n; i++){
                System.out.print(arr[i] + (i==n-1?"":" "));
            }
            System.out.println();
        }
    }
}
""",
    "FactorialUsingRecursion": """import java.util.Scanner;
public class FactorialUsingRecursion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long n = sc.nextLong();
            System.out.println(fact(n));
        }
    }
    static long fact(long n){
        if(n<=1) return 1;
        return n * fact(n-1);
    }
}
""",
    "MaximumSubarraySum": """import java.util.Scanner;
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
""",
    "MergingTwoSortedArrays": """import java.util.Scanner;
public class MergingTwoSortedArrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0; i<n; i++) a[i] = sc.nextInt();
        int m = sc.nextInt();
        int[] b = new int[m];
        for(int i=0; i<m; i++) b[i] = sc.nextInt();
        int i=0, j=0;
        while(i<n && j<m){
            if(a[i] <= b[j]) System.out.print(a[i++] + " ");
            else System.out.print(b[j++] + " ");
        }
        while(i<n) System.out.print(a[i++] + " ");
        while(j<m) System.out.print(b[j++] + " ");
        System.out.println();
    }
}
""",
    "MajorityElement": """import java.util.Scanner;
public class MajorityElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int can = -1, votes = 0;
        for(int i=0; i<n; i++){
            int x = sc.nextInt();
            if(votes == 0){
                can = x;
                votes = 1;
            } else if(can == x){
                votes++;
            } else {
                votes--;
            }
        }
        System.out.println(can);
    }
}
""",
    "MaximumAscendingSubarraySum": """import java.util.Scanner;
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
""",
    "DivisionOfTwoIntegersUsingBinarySearch": """import java.util.Scanner;
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
""",
    "CountingSort2": """import java.util.Scanner;
public class CountingSort2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] counts = new int[100];
        for(int i=0; i<n; i++) counts[sc.nextInt()]++;
        for(int i=0; i<100; i++){
            for(int j=0; j<counts[i]; j++){
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}
""",
    "MedianOfTwoSortedArrays": """import java.util.Scanner;
public class MedianOfTwoSortedArrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0; i<n; i++) a[i] = sc.nextInt();
        int m = sc.nextInt();
        int[] b = new int[m];
        for(int i=0; i<m; i++) b[i] = sc.nextInt();
        int[] c = new int[n+m];
        int i=0, j=0, k=0;
        while(i<n && j<m){
            if(a[i] <= b[j]) c[k++] = a[i++];
            else c[k++] = b[j++];
        }
        while(i<n) c[k++] = a[i++];
        while(j<m) c[k++] = b[j++];
        int len = n+m;
        if(len%2 == 1){
            System.out.println((double)c[len/2]);
        } else {
            System.out.println((c[len/2 - 1] + c[len/2]) / 2.0);
        }
    }
}
""",
    "CountingSort1": """import java.util.Scanner;
public class CountingSort1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] counts = new int[100];
        for(int i=0; i<n; i++) counts[sc.nextInt()]++;
        for(int i=0; i<100; i++){
            System.out.print(counts[i] + (i==99 ? "" : " "));
        }
        System.out.println();
    }
}
""",
    "BucketSort": """import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
public class BucketSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        float[] arr = new float[n];
        for(int i=0; i<n; i++) arr[i] = sc.nextFloat();
        ArrayList<Float>[] buckets = new ArrayList[n];
        for(int i=0; i<n; i++) buckets[i] = new ArrayList<>();
        for(int i=0; i<n; i++){
            int idx = (int)(n * arr[i]);
            if(idx >= n) idx = n - 1;
            buckets[idx].add(arr[i]);
        }
        for(int i=0; i<n; i++) Collections.sort(buckets[i]);
        for(int i=0; i<n; i++){
            for(float v : buckets[i]) System.out.print(v + " ");
        }
        System.out.println();
    }
}
""",
    "AdditionOfTwoNumbers": """import java.util.Scanner;
public class AdditionOfTwoNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            System.out.println(sc.nextLong() + sc.nextLong());
        }
    }
}
""",
    "CountingSetBits": """import java.util.Scanner;
public class CountingSetBits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            System.out.println(Long.bitCount(sc.nextLong()));
        }
    }
}
""",
    "ToggleKthBit": """import java.util.Scanner;
public class ToggleKthBit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long n = sc.nextLong();
            int k = sc.nextInt();
            System.out.println(n ^ (1L << k));
        }
    }
}
""",
    "DivisionWithBinarySearch": """import java.util.Scanner;
public class DivisionWithBinarySearch {
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
""",
    "FindTriplets": """import java.util.Scanner;
import java.util.Arrays;
public class FindTriplets {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0; i<n; i++) a[i] = sc.nextInt();
        Arrays.sort(a);
        boolean found = false;
        for(int i=0; i<n-2; i++){
            int l=i+1, r=n-1;
            while(l<r){
                int s = a[i]+a[l]+a[r];
                if(s==0){
                    System.out.println(a[i]+" "+a[l]+" "+a[r]);
                    found = true;
                    l++; r--;
                } else if(s<0) l++;
                else r--;
            }
        }
        if(!found) System.out.println("No Triplet Found");
    }
}
""",
    "CheckKthBit": """import java.util.Scanner;
public class CheckKthBit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long n = sc.nextLong();
            int k = sc.nextInt();
            if((n & (1L << k)) != 0) System.out.println("SET");
            else System.out.println("NOT SET");
        }
    }
}
""",
    "ThreeNPlusOneProblem": """import java.util.Scanner;
public class ThreeNPlusOneProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int i = sc.nextInt(), j = sc.nextInt();
            int maxCycles = 0;
            int start = Math.min(i, j);
            int end = Math.max(i, j);
            for(int n=start; n<=end; n++){
                long curr = n;
                int cycles = 1;
                while(curr != 1){
                    if(curr % 2 == 1) curr = 3 * curr + 1;
                    else curr /= 2;
                    cycles++;
                }
                if(cycles > maxCycles) maxCycles = cycles;
            }
            System.out.println(i + " " + j + " " + maxCycles);
        }
    }
}
""",
    "StringHackerRank": """import java.util.Scanner;
public class StringHackerRank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            String t = "hackerrank";
            int j = 0;
            for(int i=0; i<s.length() && j<t.length(); i++){
                if(s.charAt(i) == t.charAt(j)) j++;
            }
            System.out.println(j == t.length() ? "YES" : "NO");
        }
    }
}
""",
    "FindDuplicateCharactersUsingBitManipulation": """import java.util.Scanner;
public class FindDuplicateCharactersUsingBitManipulation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            long seen = 0, dups = 0;
            for(int i=0; i<s.length(); i++){
                char c = s.charAt(i);
                if(c >= 'a' && c <= 'z'){
                    long bit = 1L << (c - 'a');
                    if((seen & bit) != 0) dups |= bit;
                    seen |= bit;
                }
            }
            for(int i=0; i<26; i++){
                if((dups & (1L << i)) != 0){
                    System.out.print((char)('a' + i) + " ");
                }
            }
            System.out.println();
        }
    }
}
""",
    "BorderOfAString": """import java.util.Scanner;
public class BorderOfAString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            int[] lps = new int[s.length()];
            int len = 0, i = 1;
            while(i < s.length()){
                if(s.charAt(i) == s.charAt(len)){
                    len++; lps[i] = len; i++;
                } else {
                    if(len != 0) len = lps[len - 1];
                    else { lps[i] = 0; i++; }
                }
            }
            System.out.println(lps[s.length()-1]);
        }
    }
}
""",
    "PeriodOfAString": """import java.util.Scanner;
public class PeriodOfAString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            int n = s.length();
            int[] lps = new int[n];
            int len = 0, i = 1;
            while(i < n){
                if(s.charAt(i) == s.charAt(len)){
                    len++; lps[i] = len; i++;
                } else {
                    if(len != 0) len = lps[len - 1];
                    else { lps[i] = 0; i++; }
                }
            }
            int l = lps[n-1];
            if(l > 0 && n % (n - l) == 0){
                System.out.println(n - l);
            } else {
                System.out.println(n);
            }
        }
    }
}
""",
    "CamelCase": """import java.util.Scanner;
public class CamelCase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            int words = 1;
            for(int i=0; i<s.length(); i++){
                if(Character.isUpperCase(s.charAt(i))) words++;
            }
            System.out.println(s.isEmpty() ? 0 : words);
        }
    }
}
""",
    "BinaryGcd": """import java.util.Scanner;
public class BinaryGcd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long a = sc.nextLong();
            long b = sc.nextLong();
            System.out.println(gcd(a, b));
        }
    }
    static long gcd(long a, long b){
        if(a == 0) return b;
        if(b == 0) return a;
        int shift;
        for(shift = 0; ((a | b) & 1) == 0; ++shift){
            a >>= 1; b >>= 1;
        }
        while((a & 1) == 0) a >>= 1;
        do {
            while((b & 1) == 0) b >>= 1;
            if(a > b){ long t = b; b = a; a = t; }
            b -= a;
        } while(b != 0);
        return a << shift;
    }
}
""",
    "WaterJugProblem": """import java.util.Scanner;
public class WaterJugProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextInt()){
            int x = sc.nextInt(), y = sc.nextInt(), z = sc.nextInt();
            if(x + y < z) System.out.println("No");
            else if(x == z || y == z || x + y == z) System.out.println("Yes");
            else if(z % gcd(x, y) == 0) System.out.println("Yes");
            else System.out.println("No");
        }
    }
    static int gcd(int a, int b){ return b==0 ? a : gcd(b, a%b); }
}
""",
    "ExtendedEuclid": """import java.util.Scanner;
public class ExtendedEuclid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long a = sc.nextLong(), b = sc.nextLong();
            long[] res = extGCD(a, b);
            System.out.println(res[0] + " " + res[1] + " " + res[2]);
        }
    }
    static long[] extGCD(long a, long b){
        if(b == 0) return new long[]{a, 1, 0};
        long[] res = extGCD(b, a%b);
        long gcd = res[0], x1 = res[1], y1 = res[2];
        return new long[]{gcd, y1, x1 - (a/b)*y1};
    }
}
""",
    "FordFulkersonAlgorithm": """import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
public class FordFulkersonAlgorithm {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int v = sc.nextInt(), e = sc.nextInt();
        int[][] graph = new int[v][v];
        for(int i=0; i<e; i++){
            graph[sc.nextInt()][sc.nextInt()] = sc.nextInt();
        }
        int source = sc.nextInt(), sink = sc.nextInt();
        System.out.println(fordFulkerson(graph, source, sink, v));
    }
    static boolean bfs(int[][] rGraph, int s, int t, int[] parent, int V){
        boolean[] visited = new boolean[V];
        Queue<Integer> q = new LinkedList<>();
        q.add(s); visited[s] = true; parent[s] = -1;
        while(!q.isEmpty()){
            int u = q.poll();
            for(int v=0; v<V; v++){
                if(!visited[v] && rGraph[u][v] > 0){
                    if(v == t){ parent[v] = u; return true; }
                    q.add(v); visited[v] = true; parent[v] = u;
                }
            }
        }
        return false;
    }
    static int fordFulkerson(int[][] graph, int s, int t, int V){
        int[][] rGraph = new int[V][V];
        for(int u=0; u<V; u++)
            for(int v=0; v<V; v++)
                rGraph[u][v] = graph[u][v];
        int[] parent = new int[V];
        int maxFlow = 0;
        while(bfs(rGraph, s, t, parent, V)){
            int pathFlow = Integer.MAX_VALUE;
            for(int v=t; v!=s; v=parent[v])
                pathFlow = Math.min(pathFlow, rGraph[parent[v]][v]);
            for(int v=t; v!=s; v=parent[v]){
                int u = parent[v];
                rGraph[u][v] -= pathFlow;
                rGraph[v][u] += pathFlow;
            }
            maxFlow += pathFlow;
        }
        return maxFlow;
    }
}
""",
    "WildCardPatterns": """import java.util.Scanner;
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
""",
    "CoinChangeProblem": """import java.util.Scanner;
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
""",
    "MinimumCostPath": """import java.util.Scanner;
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
""",
    "RottenOranges": """import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
public class RottenOranges {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int r = sc.nextInt(), c = sc.nextInt();
        int[][] grid = new int[r][c];
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                grid[i][j] = sc.nextInt();
                if(grid[i][j] == 2) q.add(new int[]{i, j});
                else if(grid[i][j] == 1) fresh++;
            }
        }
        int time = 0;
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        while(!q.isEmpty() && fresh > 0){
            int size = q.size();
            for(int i=0; i<size; i++){
                int[] curr = q.poll();
                for(int[] d : dirs){
                    int nx = curr[0]+d[0], ny = curr[1]+d[1];
                    if(nx>=0 && nx<r && ny>=0 && ny<c && grid[nx][ny] == 1){
                        grid[nx][ny] = 2; fresh--; q.add(new int[]{nx, ny});
                    }
                }
            }
            time++;
        }
        System.out.println(fresh == 0 ? time : -1);
    }
}
""",
    "SpirallyTraverseMatrix": """import java.util.Scanner;
public class SpirallyTraverseMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int r = sc.nextInt(), c = sc.nextInt();
        int[][] mat = new int[r][c];
        for(int i=0; i<r; i++)
            for(int j=0; j<c; j++)
                mat[i][j] = sc.nextInt();
        int top=0, bottom=r-1, left=0, right=c-1;
        while(top<=bottom && left<=right){
            for(int i=left; i<=right; i++) System.out.print(mat[top][i]+" ");
            top++;
            for(int i=top; i<=bottom; i++) System.out.print(mat[i][right]+" ");
            right--;
            if(top<=bottom){
                for(int i=right; i>=left; i--) System.out.print(mat[bottom][i]+" ");
                bottom--;
            }
            if(left<=right){
                for(int i=bottom; i>=top; i--) System.out.print(mat[i][left]+" ");
                left++;
            }
        }
        System.out.println();
    }
}
""",
    "TugOfWar": """import java.util.Scanner;
public class TugOfWar {
    static int minDiff;
    static boolean[] bestSol;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        int total = 0;
        for(int i=0; i<n; i++){ arr[i] = sc.nextInt(); total += arr[i]; }
        minDiff = Integer.MAX_VALUE;
        bestSol = new boolean[n];
        boolean[] currElements = new boolean[n];
        tugOfWar(arr, n, currElements, 0, 0, total, 0);
        for(int i=0; i<n; i++) if(bestSol[i]) System.out.print(arr[i]+" ");
        System.out.println();
        for(int i=0; i<n; i++) if(!bestSol[i]) System.out.print(arr[i]+" ");
        System.out.println();
    }
    static void tugOfWar(int[] arr, int n, boolean[] currElements, int selected, int sum, int total, int currIdx){
        if(currIdx == n) return;
        if((n/2 - selected) > (n - currIdx)) return;
        tugOfWar(arr, n, currElements, selected, sum, total, currIdx+1);
        selected++; sum += arr[currIdx]; currElements[currIdx] = true;
        if(selected == n/2){
            if(Math.abs(total/2 - sum) < minDiff){
                minDiff = Math.abs(total/2 - sum);
                for(int i=0; i<n; i++) bestSol[i] = currElements[i];
            }
        } else {
            tugOfWar(arr, n, currElements, selected, sum, total, currIdx+1);
        }
        currElements[currIdx] = false;
    }
}
"""
}

# The prompt mentions week1, week2, week3 structure if there is no better existing structure.
# I will divide 34 problems into week1/Java, week2/Java, week3/Java, week4/Java
def get_week(idx):
    if idx <= 10: return "week1"
    if idx <= 20: return "week2"
    if idx <= 30: return "week3"
    return "week4"

keys = list(problems.keys())
for idx, key in enumerate(keys, 1):
    week_dir = get_week(idx)
    target_dir = os.path.join(week_dir, "Java")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, key + ".java"), "w") as f:
        f.write(problems[key])

print("Generated 34 Java files.")
