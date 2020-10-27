import java.io.*;
import java.util.*;

public class Main {
    private static char[][] map;
    private static int bx, by, rx, ry, N, M;
    static int dx[] = { -1, 0, 1, 0 };
    static int dy[] = { 0, 1, 0, -1 };
    private static int result;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new char[N][M];

        for (int i = 0; i < N; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                map[i][j] = input[j];
                if (map[i][j] == 'B') {
                    bx = i;
                    by = j;
                } else if (map[i][j] == 'R') {
                    rx = i;
                    ry = j;
                }
            }
        }
        result = 11;
        for (int i = 0; i < 4; i++) {
            dfs(rx, ry, bx, by, i, 1);
        }
        if (result == 11)
            System.out.println(-1);
        else
            System.out.println(result);
    }

    private static void dfs(int Rx, int Ry, int Bx, int By, int dir, int cnt) {
        if (cnt >= result)
            return;
        int redMove = 0;
        int blueMove = 0;
        while (map[Bx + dx[dir]][By + dy[dir]] != '#') {
            Bx += dx[dir];
            By += dy[dir];
            blueMove++;
            if (map[Bx][By] == 'O')
                return;
        }
        while (map[Rx + dx[dir]][Ry + dy[dir]] != '#') {
            Rx += dx[dir];
            Ry += dy[dir];
            redMove++;
            if (map[Rx][Ry] == 'O') {
                if (result > cnt)
                    result = cnt;
                return;
            }
        }
        if (Rx == Bx && Ry == By) {
            if (blueMove > redMove) {
                Bx -= dx[dir];
                By -= dy[dir];
            } else {
                Rx -= dx[dir];
                Ry -= dy[dir];
            }
        }

        for (int i = 0; i < 4; i++) {
            if (dir != i)
                dfs(Rx, Ry, Bx, By, i, cnt + 1);
        }
    }
}
