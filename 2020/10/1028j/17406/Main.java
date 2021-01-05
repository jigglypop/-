import java.io.*;
import java.util.*;

public class Main {
    public static int[][] map;
    public static int[][] order;
    public static int[][] temps;
    public static int Min;
    public static int Y;
    public static int X;
    public static int K;

    public static void tern(int sy, int sx, int ey, int ex, int depth, int N, int Y, int X) {
        int[][] _nums = new int[N][N];
        int py = sy;
        int px = sx;

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                _nums[y][x] = map[y + py][x + px];
            }
        }
        sy = 0;
        sx = 0;
        ey = N - 1;
        ex = N - 1;
        while (depth >= 1) {
            int y = sy;
            int x = sx;
            int d = depth;
            while (x < d) {
                x += 1;
                _nums[y][x] = map[y + py][x + px - 1];
            }
            while (y < d) {
                y += 1;
                _nums[y][x] = map[y + py - 1][x + px];
            }
            while (x > sx) {
                x -= 1;
                _nums[y][x] = map[y + py][x + px + 1];
            }
            while (y > sy) {
                y -= 1;
                _nums[y][x] = map[y + py + 1][x + px];
            }
            sy += 1;
            sx += 1;
            ey += 1;
            ex += 1;
            depth -= 1;
        }
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                map[y + py][x + px] = _nums[y][x];
            }
        }

    }

    public static void perm(int k, int N, int[] nums, int[] choice, int used, int Y, int X) {
        if (k == N) {
            for (int i : choice) {
                int dy = order[i][0];
                int dx = order[i][1];
                int s = order[i][2];
                tern(dy - s - 1, dx - s - 1, dy + s - 1, dx + s - 1, 2 * s, 2 * s + 1, Y, X);
                int tempMin = 1000000000;
                for (int y = 0; y < Y; y++) {
                    int sums = 0;
                    for (int x = 0; x < X; x++) {
                        sums += map[y][x];
                    }
                    tempMin = Math.min(tempMin, sums);
                }
                Min = Math.min(tempMin, Min);
            }
            // for (int y = 0; y < Y; y++) {
            // for (int x = 0; x < X; x++) {
            // System.out.printf("%d ", map[y][x]);
            // }
            // System.out.println();
            // }
            for (int y = 0; y < Y; y++) {
                for (int x = 0; x < X; x++) {
                    map[y][x] = temps[y][x];
                }
            }
            return;
        }
        for (int i = 0; i < N; i++) {
            if ((used & (1 << i)) != 0)
                continue;
            choice[k] = i;
            perm(k + 1, N, nums, choice, used | (1 << i), Y, X);
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int Y = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        map = new int[Y][X];
        Min = 1000000000;
        for (int y = 0; y < Y; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < X; x++) {
                map[y][x] = Integer.parseInt(st.nextToken());
            }
        }
        temps = new int[Y][X];
        for (int y = 0; y < Y; y++) {
            for (int x = 0; x < X; x++) {
                temps[y][x] = map[y][x];
            }
        }
        order = new int[K][3];
        for (int y = 0; y < K; y++) {
            st = new StringTokenizer(br.readLine());
            int sy = Integer.parseInt(st.nextToken());
            int sx = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            order[y][0] = sy;
            order[y][1] = sx;
            order[y][2] = s;
        }
        int[] nums = new int[K];
        for (int i = 0; i < K; i++) {
            nums[i] = i;
        }
        int[] choice = new int[K];

        perm(0, K, nums, choice, 0, Y, X);
        System.out.println(Min);

    }

}
