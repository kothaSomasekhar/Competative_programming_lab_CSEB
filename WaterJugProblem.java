import java.util.Scanner;
public class WaterJugProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextInt()){
            int x = sc.nextInt(), y = sc.nextInt(), z = sc.nextInt();
            if(x + y < z) System.out.println("No");
            else if(x == z || y == z || x + y == z) System.out.println("Yes");
            else if(z % gcd(x, y) == 0) System.out.println("Yes");
            else System.out.println("No");
        }
    }
    static int gcd(int a, int b){ return b==0 ? a : gcd(b, a%b); }
}
