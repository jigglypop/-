import java.io.*;
import java.util.*;

public class Main {
    public static int[][] nums = { { 1, 2, 3, 4, 5 }, { 6, 7, 8, 9, 10 }, { 11, 12, 13, 14, 15 },
            { 16, 17, 18, 19, 20 }, { 21, 22, 23, 24, 25 } };

    public static void tern(int sy, int sx, int ey, int ex, int depth, int N) {
        int[][] _nums = new int[N][N];
        for (int y = sy; y <= ey; y++) {
            for (int x = sx; x <= ex; x++) {
                _nums[y][x] = nums[y - sy][x - sx];
            }
        }
        while (depth >= 1) {
            int y = sy;
            int x = sx;
            int d = depth;
            while (x < d) {
                x += 1;
                _nums[y][x] = nums[y][x - 1];
            }
            while (y < d) {
                y += 1;
                _nums[y][x] = nums[y - 1][x];
            }
            while (x > sx) {
                x -= 1;
                _nums[y][x] = nums[y][x + 1];
            }
            while (y > sy) {
                y -= 1;
                _nums[y][x] = nums[y + 1][x];
            }
            sy += 1;
            sx += 1;
            ey += 1;
            ex += 1;
            depth -= 1;
        }
        for (int[] n : _nums) {
            for (int i : n) {
                System.out.printf("%d ", i);
            }
            System.out.println();
        }

    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        tern(0, 0, 4, 4, 4, 5);
    }
}
