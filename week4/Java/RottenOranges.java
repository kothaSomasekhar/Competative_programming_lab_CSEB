import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
public class RottenOranges {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int r = sc.nextInt(), c = sc.nextInt();
        int[][] grid = new int[r][c];
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                grid[i][j] = sc.nextInt();
                if(grid[i][j] == 2) q.add(new int[]{i, j});
                else if(grid[i][j] == 1) fresh++;
            }
        }
        int time = 0;
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        while(!q.isEmpty() && fresh > 0){
            int size = q.size();
            for(int i=0; i<size; i++){
                int[] curr = q.poll();
                for(int[] d : dirs){
                    int nx = curr[0]+d[0], ny = curr[1]+d[1];
                    if(nx>=0 && nx<r && ny>=0 && ny<c && grid[nx][ny] == 1){
                        grid[nx][ny] = 2; fresh--; q.add(new int[]{nx, ny});
                    }
                }
            }
            time++;
        }
        System.out.println(fresh == 0 ? time : -1);
    }
}
