import java.util.Scanner;
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
