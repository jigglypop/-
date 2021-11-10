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
    static StringTokenizer st;

    public static int[] dijkstra(List<Edge>[] graph, int start, int N) {
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        PriorityQueue<Edge> PQ = new PriorityQueue<>();
        PQ.add(new Edge(start, 0));
        dist[start] = 0;
        while (!PQ.isEmpty()) {
            Edge x = PQ.remove();
            int u = x.to;
            int w = x.cost;
            if (dist[u] < w)
                continue;
            for (Edge y : graph[u]) {
                int v = y.to;
                int dw = y.cost;
                if (dist[v] > dist[u] + dw) {
                    dist[v] = dist[u] + dw;
                    PQ.add(new Edge(v, dist[v]));
                }
            }
        }
        return dist;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(br.readLine());
        List<Edge>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<Edge>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new Edge(b, c));
        }
        int[] dist = dijkstra(graph, start, n);
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                sb.append("INF\n");
            } else {
                sb.append(dist[i]).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}