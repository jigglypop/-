// import java.io.FileInputStream;
// import java.util.*;

// class Edge implements Comparable<Edge> {
// int to, cost;

// Edge(int to, int cost) {
// this.to = to;
// this.cost = cost;
// }

// @Override
// public int compareTo(Edge that) {
// return Integer.compare(this.cost, that.cost);
// }
// }

// public class Main {
// static final int inf = 1000000000;

// public static void main(String args[]) throws Exception {
// System.setIn(new FileInputStream("./input.txt"));
// Scanner sc = new Scanner(System.in);
// int n = sc.nextInt();
// List<Edge>[] graph = (List<Edge>[]) new List[n + 1];
// for (int i = 1; i <= n; i++) {
// graph[i] = new ArrayList<Edge>();
// }
// int m = sc.nextInt();
// int start = sc.nextInt();
// for (int i = 0; i < m; i++) {
// int a = sc.nextInt();
// int b = sc.nextInt();
// int c = sc.nextInt();
// graph[a].add(new Edge(b, c));
// }
// int[] dist = new int[n + 1];
// boolean[] check = new boolean[n + 1];
// for (int i = 1; i <= n; i++) {
// dist[i] = inf;
// check[i] = false;
// }
// dist[start] = 0;
// PriorityQueue<Edge> q = new PriorityQueue<>();
// q.add(new Edge(start, 0));
// while (!q.isEmpty()) {
// int x = q.remove().to;
// if (check[x])
// continue;
// check[x] = true;
// for (Edge y : graph[x]) {
// int v = y.to;
// int dw = y.cost;
// if (dist[v] > dist[x] + dw) {
// dist[v] = dist[x] + dw;
// q.add(new Edge(v, dist[v]));
// }
// }
// }
// for (int i = 1; i <= n; i++) {
// if (dist[i] == inf) {
// System.out.println("INF");
// } else {
// System.out.println(dist[i]);
// }
// }
// }
// }