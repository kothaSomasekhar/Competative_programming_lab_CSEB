import java.util.Scanner;
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
