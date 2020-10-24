import java.io.*;
import java.util.*;

public class Main {
    static int INF = 1000000001;
    static StringTokenizer st;

    public static int[][] floyd(int[][] graph, int N) {
        for (int k = 1; k <= N; k++) {
            for (int y = 1; y <= N; y++) {
                for (int x = 1; x <= N; x++) {
                    if (graph[y][x] > graph[y][k] + graph[k][x]) {
                        graph[y][x] = graph[y][k] + graph[k][x];
                    }
                }
            }
        }
        return graph;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[][] graph = new int[n + 1][n + 1];
        for (int y = 1; y <= n; y++) {
            for (int x = 1; x <= n; x++) {
                if (y == x) {
                    graph[y][x] = 0;
                } else {
                    graph[y][x] = INF;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (graph[a][b] > c) {
                graph[a][b] = c;
            }
        }
        int[][] _graph = floyd(graph, n);
        StringBuilder sb = new StringBuilder();
        for (int y = 1; y <= n; y++) {
            for (int x = 1; x <= n; x++) {
                if (_graph[y][x] == INF) {
                    _graph[y][x] = 0;
                }
                sb.append(_graph[y][x]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}