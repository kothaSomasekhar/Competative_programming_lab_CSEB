import java.util.Scanner;
public class ExtendedEuclid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            long a = sc.nextLong(), b = sc.nextLong();
            long[] res = extGCD(a, b);
            System.out.println(res[0] + " " + res[1] + " " + res[2]);
        }
    }
    static long[] extGCD(long a, long b){
        if(b == 0) return new long[]{a, 1, 0};
        long[] res = extGCD(b, a%b);
        long gcd = res[0], x1 = res[1], y1 = res[2];
        return new long[]{gcd, y1, x1 - (a/b)*y1};
    }
}
