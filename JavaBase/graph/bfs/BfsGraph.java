import java.io.FileInputStream;
import java.util.*;

class Pair {
    int y;
    int x;

    Pair(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class BfsGraph {

    static int[][] matrix;

    public static void bfs(int sy, int sx, int Y, int X, int cnt) {
        int[] dy = { 1, -1, 0, 0 };
        int[] dx = { 0, 0, 1, -1 };

        int[][] visited = new int[Y][X];

        Queue<Pair> Q = new LinkedList<Pair>();
        Q.add(new Pair(sy, sx));
        visited[sy][sx] = cnt;

        while (!Q.isEmpty()) {
            Pair p = Q.remove();
            int y = p.y;
            int x = p.x;
            for (int i = 0; i < 8; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= nx && nx < X && 0 <= ny && ny < Y) {
                    if (matrix[ny][nx] == 1 && visited[ny][nx] == 0) {
                        Q.add(new Pair(ny, nx));
                        visited[ny][nx] = cnt;
                    }
                }
            }
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./inputB.txt"));
        Scanner sc = new Scanner(System.in);

        while (true) {
            int X = sc.nextInt();
            int Y = sc.nextInt();
            if (Y == 0 && X == 0) {
                break;
            }
            int[][] matrix = new int[Y][X];
            for (int y = 0; y < Y; y++) {
                for (int x = 0; x < X; x++) {
                    matrix[y][x] = sc.nextInt();
                }
            }
            int cnt = 0;
            int[][] visited = new int[Y][X];
            for (int y = 0; y < Y; y++) {
                for (int x = 0; x < X; x++) {
                    if (matrix[y][x] == 1 && visited[y][x] == 0) {
                        bfs(y, x, Y, X, ++cnt);
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}