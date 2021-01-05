import java.io.*;
import java.util.*;

class Edge {
    int to, cost;

    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}

public class Main {
    public static int[] bfs(int N, ArrayList<Edge>[] tree, int start) {
        boolean[] check = new boolean[N + 1];
        int[] dist = new int[N + 1];
        Queue<Integer> Q = new LinkedList<Integer>();
        Q.add(start);
        check[start] = true;
        while (!Q.isEmpty()) {
            int u = Q.remove();
            for (Edge t : tree[u]) {
                int v = t.to;
                int cost = t.cost;
                if (check[v] == false) {
                    check[v] = true;
                    dist[v] = dist[u] + cost;
                    Q.add(v);
                }
            }
        }
        return dist;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./diameter.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Edge>[] tree = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            tree[i] = new ArrayList<Edge>();
        }
        for (int i = 1; i <= N; i++) {
            int x = sc.nextInt();
            while (true) {
                int y = sc.nextInt();
                if (y == -1)
                    break;
                int z = sc.nextInt();
                tree[x].add(new Edge(y, z));
            }
        }

        int[] dist = bfs(N, tree, 1);
        int start = 1;
        for (int i = 2; i <= N; i++) {
            if (dist[i] > dist[start]) {
                start = i;
            }
        }
        dist = bfs(N, tree, start);
        int ans = dist[1];
        for (int i = 2; i <= N; i++) {
            if (ans < dist[i]) {
                ans = dist[i];
            }
        }
        System.out.println(ans);

    }
}
