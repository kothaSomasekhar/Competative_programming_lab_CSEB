import java.util.Scanner;
public class CamelCase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            int words = 1;
            for(int i=0; i<s.length(); i++){
                if(Character.isUpperCase(s.charAt(i))) words++;
            }
            System.out.println(s.isEmpty() ? 0 : words);
        }
    }
}
