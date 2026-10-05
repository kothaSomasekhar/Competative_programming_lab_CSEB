import java.util.Scanner;
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
