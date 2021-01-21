import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    static int[][] triangle = new int[401][801];
    static int[][] sums = new int[401][801];
    static int result;
    static int N;

    static void go(int row, int left, int right, int sum) {
        if (row < 1 || row > N)
            return;
        if (left < 1 || right > 2 * row - 1)
            return;
        sum += sums[row][right] - sums[row][left - 1];
        if (sum > result)
            result = sum;
        if (left % 2 == 0) {
            go(row - 1, left - 2, right, sum);
        } else {
            go(row + 1, left, right + 2, sum);
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = 0;
        while (true) {
            t += 1;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            result = -1000000000;
            if (N == 0) {
                break;
            }
            for (int y = 1; y <= N; y++) {
                for (int x = 1; x <= 2 * y - 1; x++) {
                    triangle[y][x] = Integer.parseInt(st.nextToken());
                    sums[y][x] = sums[y][x - 1] + triangle[y][x];
                }
            }
            for (int y = 1; y <= N; y++) {
                for (int x = 1; x <= 2 * y - 1; x++) {
                    go(y, x, x, 0);
                }
            }
            System.out.printf("%d. %d\n", t, result);

        }
    }
}
