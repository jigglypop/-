import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] DP = new int[N + 1];
        DP[1] = 0;
        for (int i = 2; i <= N; i++) {
            DP[i] = DP[i - 1] + 1;
            if (i % 2 == 0 && DP[i] > DP[i / 2] + 1) {
                DP[i] = DP[i / 2] + 1;
            }
            if (i % 3 == 0 && DP[i] > DP[i / 3] + 1) {
                DP[i] = DP[i / 3] + 1;
            }
        }
        System.out.println(DP[N]);
    }
}
