import java.io.FileInputStream;
import java.util.Scanner;
import java.util.*;

public class b {

    public static void dfs(ArrayList<Integer>[] graph, boolean[] visited, int u) {
        if (visited[u]) {
            return;
        }
        visited[u] = true;
        for (int v : graph[u]) {
            if (visited[v] == false) {
                dfs(graph, visited, v);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./b.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        ArrayList<Integer>[] graph = new ArrayList[N + 1];
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
        boolean[] visited = new boolean[N + 1];
        int result = 0;
        for (int i = 1; i <= N; i++) {
            if (visited[i] == false) {
                dfs(graph, visited, i);
                result++;
            }
        }
        System.out.println(result);

    }
}
