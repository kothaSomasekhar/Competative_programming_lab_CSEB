import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
public class FordFulkersonAlgorithm {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int v = sc.nextInt(), e = sc.nextInt();
        int[][] graph = new int[v][v];
        for(int i=0; i<e; i++){
            graph[sc.nextInt()][sc.nextInt()] = sc.nextInt();
        }
        int source = sc.nextInt(), sink = sc.nextInt();
        System.out.println(fordFulkerson(graph, source, sink, v));
    }
    static boolean bfs(int[][] rGraph, int s, int t, int[] parent, int V){
        boolean[] visited = new boolean[V];
        Queue<Integer> q = new LinkedList<>();
        q.add(s); visited[s] = true; parent[s] = -1;
        while(!q.isEmpty()){
            int u = q.poll();
            for(int v=0; v<V; v++){
                if(!visited[v] && rGraph[u][v] > 0){
                    if(v == t){ parent[v] = u; return true; }
                    q.add(v); visited[v] = true; parent[v] = u;
                }
            }
        }
        return false;
    }
    static int fordFulkerson(int[][] graph, int s, int t, int V){
        int[][] rGraph = new int[V][V];
        for(int u=0; u<V; u++)
            for(int v=0; v<V; v++)
                rGraph[u][v] = graph[u][v];
        int[] parent = new int[V];
        int maxFlow = 0;
        while(bfs(rGraph, s, t, parent, V)){
            int pathFlow = Integer.MAX_VALUE;
            for(int v=t; v!=s; v=parent[v])
                pathFlow = Math.min(pathFlow, rGraph[parent[v]][v]);
            for(int v=t; v!=s; v=parent[v]){
                int u = parent[v];
                rGraph[u][v] -= pathFlow;
                rGraph[v][u] += pathFlow;
            }
            maxFlow += pathFlow;
        }
        return maxFlow;
    }
}
