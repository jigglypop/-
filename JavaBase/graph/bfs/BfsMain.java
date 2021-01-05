import java.io.FileInputStream;
import java.util.*;

public class BfsMain {

    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void bfs(int start) {
        Queue<Integer> Q = new LinkedList<>();
        Q.add(start);
        visited[start] = true;
        while (!Q.isEmpty()) {
            int u = Q.remove();
            System.out.print(u + " ");
            for (int v : graph[u]) {
                if (visited[v] == false) {
                    visited[v] = true;
                    Q.add(v);
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./inputA.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int V = sc.nextInt();
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
        bfs(V);
    }
}
