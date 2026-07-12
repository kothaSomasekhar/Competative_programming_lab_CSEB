import java.io.*;
import java.util.*;

public class Lengthofstring {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner sc=new Scanner(System.in);
    
    String s=sc.next();
    int length=0;
    for(char c:s.toCharArray()){
        length++;
    }
   
    System.out.println(length);
    sc.close();
    }
}
