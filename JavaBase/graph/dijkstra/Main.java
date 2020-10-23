import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {
    int to, cost;

    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge that) {
        return Integer.compare(this.cost, that.cost);
    }
}

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static StringTokenizer stk;

    public static int[] dijkstra(List<Edge>[] graph) {
        // int[] dist
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());
        int start = Integer.parseInt(br.readLine());
        List<Edge>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<Edge>();
        }
        for (int i = 0; i < m; i++) {
            stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            int c = Integer.parseInt(stk.nextToken());
            graph[a].add(new Edge(b, c));
        }
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.add(new Edge(start, 0));
        while (!pq.isEmpty()) {
            Edge x = pq.remove();
            int u = x.to;
            int w = x.cost;
            if (dist[u] < w)
                continue;
            for (Edge y : graph[u]) {
                int v = y.to;
                int dw = y.cost;
                if (dist[v] > dist[u] + dw) {
                    dist[v] = dist[u] + dw;
                    pq.add(new Edge(v, dist[v]));
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INF) {
                sb.append("INF\n");
            } else {
                sb.append(dist[i]).append("\n");

            }
        }
        System.out.println(sb.toString());
    }
}