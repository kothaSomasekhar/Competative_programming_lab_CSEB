import java.util.Scanner;
public class CalculateLengthOfString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            System.out.println(s.length());
        }
    }
}
