import java.util.Scanner;
public class FactorialUsingRecursion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long n = sc.nextLong();
            System.out.println(fact(n));
        }
    }
    static long fact(long n){
        if(n<=1) return 1;
        return n * fact(n-1);
    }
}
