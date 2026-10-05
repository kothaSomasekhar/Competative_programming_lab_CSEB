import java.util.Scanner;
public class BorderOfAString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            int[] lps = new int[s.length()];
            int len = 0, i = 1;
            while(i < s.length()){
                if(s.charAt(i) == s.charAt(len)){
                    len++; lps[i] = len; i++;
                } else {
                    if(len != 0) len = lps[len - 1];
                    else { lps[i] = 0; i++; }
                }
            }
            System.out.println(lps[s.length()-1]);
        }
    }
}
