import java.io.*;
import java.util.*;

public class Main {
    public static int Y;
    public static int X;
    public static int[] dy = { -1, 0, 1, 0 };
    public static int[] dx = { 0, 1, 0, -1 };
    public static char[][] board;
    public static int count;

    public static int dir(char word) {
        int result;
        if (word == 'U') {
            result = 0;
        } else if (word == 'R') {
            result = 1;
        } else if (word == 'D') {
            result = 2;
        } else {
            result = 3;
        }
        return result;
    }

    public static boolean go(int y, int x, int Y, int X) {
        int i = dir(board[y][x]);
        boolean[][] visited = new boolean[Y][X];
        visited[y][x] = true;
        int ny = y + dy[i];
        int nx = x + dx[i];
        while (true) {
            if (0 > ny | ny >= Y | 0 > nx | nx >= X) {
                return true;
            }
            if (visited[ny][nx] == true) {
                return false;
            }
            i = dir(board[ny][nx]);
            visited[ny][nx] = true;
            ny += dy[i];
            nx += dx[i];
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int Y = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        board = new char[Y][X];
        for (int y = 0; y < Y; y++) {
            String s = br.readLine();
            for (int x = 0; x < X; x++) {
                board[y][x] = s.charAt(x);
            }
        }
        int count = 0;
        for (int y = 0; y < Y; y++) {
            for (int x = 0; x < X; x++) {
                if (go(y, x, Y, X)) {
                    count += 1;
                }
            }
        }
        System.out.println(count);
    }
}
