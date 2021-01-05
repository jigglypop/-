import java.io.*;
import java.util.*;

public class Main {
    static int[] dy = { -1, 1, 0, 0 };
    static int[] dx = { 0, 0, -1, 1 };

    static int Max = 0;
    static int N;

    public static int go(char[][] board, int y, int x, int dy, int dx, char c) {
        int count = 0;
        int ny = y;
        int nx = x;
        while (true) {
            if (0 > ny || ny >= N || 0 > nx || nx >= N) {
                break;
            }
            if (board[ny][nx] == c) {
                count += 1;
                ny += dy;
                nx += dx;
            } else {
                break;
            }
        }
        return count;
    }

    public static int bfs(char[][] board, int sy, int sx, int cy, int cx) {
        char temp;
        temp = board[sy][sx];
        board[sy][sx] = board[cy][cx];
        board[cy][cx] = temp;
        int[][][] dict = { { { -1, 0 }, { 1, 0 } }, { { 0, 1 }, { 0, -1 } } };
        int Max_val = 0;
        for (int[][] di : dict) {
            int sums = 1;
            for (int[] d : di) {
                if (0 <= sy + d[0] && sy + d[0] < N && 0 <= sx + d[1] && sx + d[1] < N) {
                    sums += go(board, sy + d[0], sx + d[1], d[0], d[1], board[sy][sx]);
                }
            }
            Max_val = Math.max(Max_val, sums);
        }
        temp = board[sy][sx];
        board[sy][sx] = board[cy][cx];
        board[cy][cx] = temp;
        return Max_val;
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        char[][] board = new char[N][N];
        for (int y = 0; y < N; y++) {
            String s = br.readLine();
            for (int x = 0; x < N; x++) {
                board[y][x] = s.charAt(x);
            }
        }
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                for (int i = 0; i < 4; i++) {
                    int ny = y + dy[i];
                    int nx = x + dx[i];
                    if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                        int count = bfs(board, y, x, ny, nx);
                        Max = Math.max(count, Max);
                    }
                }
            }
        }
        System.out.println(Max);
    }
}
