import java.util.Scanner;
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
