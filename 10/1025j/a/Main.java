import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;
    static int[] depth;

    public static int lca(int u, int v) {
        if (depth[u] < depth[v]) {
            int temp = u;
            u = v;
            v = temp;
        }
        while (depth[u] != depth[v]) {
            u = parent[u];
        }
        while (u != v) {
            u = parent[u];
            v = parent[v];
        }
        return u;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] tree = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tree[a].add(b);
            tree[b].add(a);
        }
        parent = new int[N + 1];
        depth = new int[N + 1];
        depth[1] = 0;
        parent[1] = 1;
        Queue<Integer> Q = new LinkedList<Integer>();
        boolean[] check = new boolean[N + 1];
        check[1] = true;
        Q.add(1);
        while (!Q.isEmpty()) {
            int u = Q.remove();
            for (int v : tree[u]) {
                if (!check[v]) {
                    depth[v] = depth[u] + 1;
                    check[v] = true;
                    parent[v] = u;
                    Q.add(v);
                }
            }
        }

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            System.out.println(lca(u, v));
        }
    }
}
