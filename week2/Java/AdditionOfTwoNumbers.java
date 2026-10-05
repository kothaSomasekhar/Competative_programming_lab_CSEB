import java.util.Scanner;
public class AdditionOfTwoNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLong()){
            System.out.println(sc.nextLong() + sc.nextLong());
        }
    }
}
