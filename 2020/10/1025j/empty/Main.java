import java.io.*;
import java.util.*;

public class Main {
    // 상 하 좌 우
    static int N;
    static int[] dy = { -1, 1, 0, 0 };
    static int[] dx = { 0, 0, -1, 1 };
    static int[][] board;
    static int[] nums = { 0, 1, 2, 3 };
    static int count;

    public static void perm(int k, int[] choice) {
        if (k == 5) {
            count += 1;
            for (int i : choice) {
                System.out.printf("%d ", i);
            }
            System.out.println();
            return;
        }
        for (int i = 0; i < 4; i++) {
            choice[k] = i;
            perm(k + 1, choice);
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        for (int y = 0; y < N; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < N; x++) {
                board[y][x] = Integer.parseInt(st.nextToken());
            }
        }
        int[] choice = new int[5];
        perm(0, choice);
        System.out.println(count);
        // int[][] _board = new int[N][N];
        // for (int y = 0; y < N; y++) {
        // for (int x = 0; x < N; x++) {
        // System.out.printf("%d ", _board[y][x]);
        // }
        // System.out.println();
        // }
    }
}
