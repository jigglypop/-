import java.io.*;
import java.util.*;

public class Main {
    static int[] check;
    static StringTokenizer st;

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Integer>[] graph = new List[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        int[] check = new int[N + 1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            check[b] += 1;
        }
        Queue<Integer> Q = new LinkedList<Integer>();
        for (int i = 1; i <= N; i++) {
            if (check[i] == 0) {
                Q.add(i);
            }
        }
        while (!Q.isEmpty()) {
            int u = Q.remove();
            System.out.print(u + " ");
            for (int v : graph[u]) {
                check[v] -= 1;
                if (check[v] == 0) {
                    Q.add(v);
                }
            }
        }
        System.out.println();
    }
}