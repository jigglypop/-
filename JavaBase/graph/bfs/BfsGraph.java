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
    public static final int[] dy = { 1, -1, 0, 0, 1, -1, 1, -1 };
    public static final int[] dx = { 0, 0, 1, -1, 1, 1, -1, -1 };

    public static void bfs(int[][] board, int[][] visited, int y, int x, int cnt, int n, int m) {
        Queue<Pair> Q = new LinkedList<Pair>();
        Q.add(new Pair(y, x));
        visited[y][x] = cnt;
        while (!Q.isEmpty()) {
            Pair p = Q.remove();
            y = p.y;
            x = p.x;
            for (int i = 0; i < 8; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    if (board[ny][nx] == 1 && visited[ny][nx] == 0) {
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
            int[][] board = new int[Y][X];
            for (int y = 0; y < Y; y++) {
                for (int x = 0; x < X; x++) {
                    board[y][x] = sc.nextInt();
                }
            }
            int cnt = 0;
            int[][] visited = new int[Y][X];
            for (int y = 0; y < Y; y++) {
                for (int x = 0; x < X; x++) {
                    if (board[y][x] == 1 && visited[y][x] == 0) {
                        bfs(board, visited, y, x, ++cnt, Y, X);
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}