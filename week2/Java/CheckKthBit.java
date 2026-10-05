import java.util.Scanner;
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
