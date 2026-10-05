import java.util.Scanner;
public class StringHackerRank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            String t = "hackerrank";
            int j = 0;
            for(int i=0; i<s.length() && j<t.length(); i++){
                if(s.charAt(i) == t.charAt(j)) j++;
            }
            System.out.println(j == t.length() ? "YES" : "NO");
        }
    }
}
