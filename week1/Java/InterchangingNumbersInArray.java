import java.util.Scanner;
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
