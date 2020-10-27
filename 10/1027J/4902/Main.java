import java.io.*;
import java.util.*;

public class Main {
    public static StringTokenizer st;

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            st = new StringTokenizer(br.readLine());
            int Y = Integer.parseInt(st.nextToken());
            if (Y == 0) {
                break;
            }
            int X = (Y - 1) * 2 + 1;
            int[][] triangle = new int[Y][X];
            int mid = X / 2;
            for (int y = 0; y < Y; y++) {
                for (int x = mid - y; x < mid + y + 1; x++) {
                    triangle[y][x] = Integer.parseInt(st.nextToken());
                }
            }
            for (int y = 0; y < Y; y++) {
                for (int x = 0; x < X; x++) {
                    System.out.printf("%2d  ", triangle[y][x]);
                }
                System.out.println();
            }
        }
    }
}
