import java.io.*;
import java.util.*;


public class B {

    static int Y, X;
    static boolean[][] visited;
    static char[][] board;
    static StringTokenizer st;
    static String shapes = "|-";

    static class Pair {
        int y;
        int x;

        public Pair(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    
    static void bfs(int sy, int sx, int flag) {
        int y, x, ny, nx;
        int[][] di = {{ -1, 0 }, { 1, 0 }, { 0, 1 },{ 0, -1 }};
        int[][] dir = { { 0, 1 }, { 2, 3 } };
        char shape = shapes.charAt(flag);

        Queue<Pair> Q = new LinkedList<Pair>();
        Q.add(new Pair(sy, sx));
        visited[sy][sx] = true;

        while (!Q.isEmpty()) {
            Pair q = Q.remove();
            y = q.y;
            x = q.x;
            int[] range = dir[flag];
            for (int z : range) {
                ny = y + di[z][0];
                nx = x + di[z][1];
                if (0 <= nx && nx < X && 0 <= ny && ny < Y) {
                    if (!visited[ny][nx] && board[ny][nx] == shape) {
                        Q.add(new Pair(ny, nx));
                        visited[ny][nx] = true;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./1388.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        Y = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        visited = new boolean[Y][X];
        board = new char[Y][X];

        for (int y = 0; y < Y; y++) {
            String str = br.readLine();
            for (int x = 0; x < X; x++) {
                board[y][x] = str.charAt(x);
            }
        }
        int count = 0;
        for (int y = 0; y < Y; y++) {
            for (int x = 0; x < X; x++) {
                if (!visited[y][x]) {
                    if (board[y][x] == shapes.charAt(0)) {
                        bfs(y, x, 0);
                    } else {
                        bfs(y, x, 1);
                    }
                    count++;
                }
            }
        }
        sb.append(count);
        System.out.println(sb);
    }
}
