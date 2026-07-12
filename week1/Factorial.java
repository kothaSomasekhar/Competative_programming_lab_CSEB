import java.io.*;
import java.util.*;

public class Factorial{
    public static int recu(int val){
        if(val==1)return 1;
        return val*recu(val-1);
        
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int val=sc.nextInt();
        
        System.out.print(recu(val));
        sc.close();
    }
}
