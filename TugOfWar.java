import java.util.Scanner;
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
