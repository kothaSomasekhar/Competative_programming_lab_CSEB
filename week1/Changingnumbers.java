import java.io.*;
import java.util.*;

public class Changingnumbers {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int max=arr[0];
        int maxindex=0;
        int minindex=0;
        int min=arr[0];
        for(int i=1;i<n;i++){
            if(max>arr[i]){
                max=arr[i];
                maxindex=i;
            }
            if(min<arr[i]){
                min=arr[i];
                minindex=i;
            }
        }
        arr[minindex]=max;
        arr[maxindex]=min;
        for(int a:arr){
            System.out.print(a+" ");
        }
        sc.close();
        
    }
}
