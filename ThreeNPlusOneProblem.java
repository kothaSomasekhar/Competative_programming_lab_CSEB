import java.util.Scanner;
public class ThreeNPlusOneProblem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int i = sc.nextInt(), j = sc.nextInt();
            int maxCycles = 0;
            int start = Math.min(i, j);
            int end = Math.max(i, j);
            for(int n=start; n<=end; n++){
                long curr = n;
                int cycles = 1;
                while(curr != 1){
                    if(curr % 2 == 1) curr = 3 * curr + 1;
                    else curr /= 2;
                    cycles++;
                }
                if(cycles > maxCycles) maxCycles = cycles;
            }
            System.out.println(i + " " + j + " " + maxCycles);
        }
    }
}
