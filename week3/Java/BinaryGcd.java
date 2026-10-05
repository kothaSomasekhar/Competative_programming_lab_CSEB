import java.util.Scanner;
public class BinaryGcd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long a = sc.nextLong();
            long b = sc.nextLong();
            System.out.println(gcd(a, b));
        }
    }
    static long gcd(long a, long b){
        if(a == 0) return b;
        if(b == 0) return a;
        int shift;
        for(shift = 0; ((a | b) & 1) == 0; ++shift){
            a >>= 1; b >>= 1;
        }
        while((a & 1) == 0) a >>= 1;
        do {
            while((b & 1) == 0) b >>= 1;
            if(a > b){ long t = b; b = a; a = t; }
            b -= a;
        } while(b != 0);
        return a << shift;
    }
}
