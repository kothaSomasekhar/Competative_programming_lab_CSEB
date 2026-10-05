import java.util.Scanner;
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
