import java.io.*;
import java.util.*;

public class Main {
    static int[] DP;

    public static int go(int N) {
        if (N == 1) {
            return 0;
        } else if (DP[N] > 0) {
            return DP[N];
        }
        DP[N] = go(N - 1) + 1;
        if (N % 2 == 0) {
            int temp = go(N / 2) + 1;
            if (DP[N] > temp) {
                DP[N] = temp;
            }
        }
        if (N % 3 == 0) {
            int temp = go(N / 3) + 1;
            if (DP[N] > temp) {
                DP[N] = temp;
            }
        }
        return DP[N];

    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        DP = new int[N + 1];
        System.out.println(go(N));
    }
}
