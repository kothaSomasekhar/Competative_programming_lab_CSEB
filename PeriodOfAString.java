import java.util.Scanner;
public class PeriodOfAString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            int n = s.length();
            int[] lps = new int[n];
            int len = 0, i = 1;
            while(i < n){
                if(s.charAt(i) == s.charAt(len)){
                    len++; lps[i] = len; i++;
                } else {
                    if(len != 0) len = lps[len - 1];
                    else { lps[i] = 0; i++; }
                }
            }
            int l = lps[n-1];
            if(l > 0 && n % (n - l) == 0){
                System.out.println(n - l);
            } else {
                System.out.println(n);
            }
        }
    }
}
