import java.io.*;
import java.util.*;

class Pair implements Comparable<Pair> {
    int x;
    int y;

    public Pair(int x, int y) {
        super();
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pair that) {
        if (this.x == that.x) {
            return this.y - that.y;
        }
        return this.x - that.x;
    }

}

public class Main {

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pq.add(new Pair(x, y));
        }
        while (!pq.isEmpty()) {
            sb.append(pq.peek().x).append(" ").append(pq.poll().y).append("\n");
        }
        System.out.println(sb);
    }
}