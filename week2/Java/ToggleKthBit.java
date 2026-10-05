import java.util.Scanner;
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
