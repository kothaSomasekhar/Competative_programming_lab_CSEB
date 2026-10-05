import java.util.Scanner;
public class FindDuplicateCharactersUsingBitManipulation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextLine()){
            String s = sc.nextLine();
            long seen = 0, dups = 0;
            for(int i=0; i<s.length(); i++){
                char c = s.charAt(i);
                if(c >= 'a' && c <= 'z'){
                    long bit = 1L << (c - 'a');
                    if((seen & bit) != 0) dups |= bit;
                    seen |= bit;
                }
            }
            for(int i=0; i<26; i++){
                if((dups & (1L << i)) != 0){
                    System.out.print((char)('a' + i) + " ");
                }
            }
            System.out.println();
        }
    }
}
