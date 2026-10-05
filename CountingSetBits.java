import java.util.Scanner;
public class CountingSetBits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            System.out.println(Long.bitCount(sc.nextLong()));
        }
    }
}
