import java.io.*;
import java.util.*;

public class Main2 {
    static StringTokenizer st;
    static int[] parent;

    public static int find(int x) {
        if (parent[x] == x)
            return x;
        return parent[x] = find(parent[x]);
    }

    public static boolean union(int a, int b) {
        int x = find(a);
        int y = find(b);
        if (x != y) {
            parent[y] = x;
            return true;
        }
        return false;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            pq.add(new Edge(a, b, c));
        }
        parent = new int[V + 1];
        for (int i = 1; i <= V; i++)
            parent[i] = i;
        long result = 0;
        while (!pq.isEmpty()) {
            Edge p = pq.remove();
            if (union(p.from, p.to))
                result += p.cost;
        }
        System.out.println(result);
    }
}