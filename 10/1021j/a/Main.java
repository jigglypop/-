import java.io.FileInputStream;
import java.util.*;

class Pair {
    int y, x;

    Pair(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    public static final int[] dy = { 1, -1, 0, 0 };
    public static final int[] dx = { 0, 0, 1, -1 };

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        Scanner sc = new Scanner(System.in);
        int Y = sc.nextInt();
        int X = sc.nextInt();
        int[][] graph = new int[Y][X];
        sc.nextLine();
        for (int y = 0; y < Y; y++) {
            String s = sc.nextLine();
            for (int x = 0; x < X; x++) {
                graph[y][x] = s.charAt(x) - '0';
            }
        }
        int[][] dist = new int[Y][X];
        boolean[][] check = new boolean[Y][X];
        Queue<Pair> Q = new LinkedList<Pair>();
        Q.add(new Pair(0, 0));
        check[0][0] = true;
        dist[0][0] = 1;
        while (!Q.isEmpty()) {
            Pair q = Q.remove();
            int y = q.y;
            int x = q.x;
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= nx && nx < X && 0 <= ny && ny < Y) {
                    if (check[ny][nx] == false && graph[ny][nx] == 1) {
                        Q.add(new Pair(ny, nx));
                        dist[ny][nx] = dist[y][x] + 1;
                        check[ny][nx] = true;
                    }
                }
            }
        }
        System.out.println(dist[Y - 1][X - 1]);

    }
}
