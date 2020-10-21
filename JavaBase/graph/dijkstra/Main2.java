import java.io.*;
import java.util.*;

public class Main2 {
    static final int INF = 1000000000;

    static class Node implements Comparable<Node> {
        int len, to;
        Node next;

        public Node(int len, int to, Node next) {
            this.len = len;
            this.to = to;
            this.next = next;
        }

        @Override
        public int compareTo(Node o) {
            return this.len - o.len;
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(stk.nextToken());
        int E = Integer.parseInt(stk.nextToken());
        int start = Integer.parseInt(br.readLine());

        Node[] list = new Node[V + 1];
        for (int i = 0; i < E; i++) {
            stk = new StringTokenizer(br.readLine());
            int st = Integer.parseInt(stk.nextToken());
            int end = Integer.parseInt(stk.nextToken());
            int len = Integer.parseInt(stk.nextToken());

            list[st] = new Node(len, end, list[st]);
        }

        int distance[] = new int[V + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.offer(new Node(0, start, null));
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (distance[node.to] < node.len)
                continue;

            for (Node n = list[node.to]; n != null; n = n.next) {
                if (distance[n.to] > distance[node.to] + n.len) {
                    distance[n.to] = distance[node.to] + n.len;
                    pq.offer(new Node(distance[n.to], n.to, null));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            if (distance[i] == Integer.MAX_VALUE)
                sb.append("INF\n");
            else
                sb.append(distance[i]).append("\n");
        }
        System.out.println(sb.toString());
    }
}
