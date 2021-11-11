import java.io.*;
import java.util.*;

public class MainD {
    static StringTokenizer st;
    static int N, M, a, b, c;
    static int[][] graph;
    static ArrayList<Integer>[] tree;
    static boolean[] visited;
    static int result;

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("./1240.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N + 1][N + 1];
        tree = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            for (int j = 0; j < N + 1; j++) {
                graph[i][j] = 123456789;
                if (i == j)
                    graph[i][j] = 0;
            }
        }
        for (int i = 0; i < N + 1; i++)
            tree[i] = new ArrayList<Integer>();

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            graph[a][b] = c;
            graph[b][a] = c;
            tree[a].add(b);
            tree[b].add(a);
        }
        for (int k = 0; k < N + 1; k++) {
            for (int i = 0; i < N + 1; i++) {
                for (int j = 0; j < N + 1; j++) {
                    if (graph[i][j] > graph[i][k] + graph[k][j]) {
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            System.out.println(graph[a][b]);
        }
    }
}
