import java.io.FileInputStream;
import java.util.*;

public class DfsGraph {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void dfs(int u) {
        if (visited[u]) {
            return;
        }
        visited[u] = true;
        System.out.print(u + " ");
        for (int v : graph[u]) {
            if (visited[v] == false) {
                dfs(v);
            }
        }

    }

    public static void main(String[] args) throws Exception {

        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int start = sc.nextInt();
        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);

        }
        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }
        visited = new boolean[N + 1];
        dfs(start);
    }
}
