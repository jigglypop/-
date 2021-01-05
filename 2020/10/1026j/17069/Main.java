import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int board[][] = new int[N][N];
        long dp[][][] = new long[3][N][N];
        for (int y = 0; y < N; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < N; x++) {
                board[y][x] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0][0][1] = 1;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (x + 1 < N && board[y][x + 1] == 0) {
                    dp[0][y][x + 1] += dp[0][y][x];
                    dp[0][y][x + 1] += dp[1][y][x];
                }
                if (x + 1 < N && y + 1 < N && board[y + 1][x] == 0 && board[y + 1][x + 1] == 0
                        && board[y][x + 1] == 0) {
                    dp[1][y + 1][x + 1] += dp[0][y][x];
                    dp[1][y + 1][x + 1] += dp[2][y][x];
                    dp[1][y + 1][x + 1] += dp[1][y][x];
                }
                if (y + 1 < N && board[y + 1][x] == 0) {
                    dp[2][y + 1][x] += dp[2][y][x];
                    dp[2][y + 1][x] += dp[1][y][x];
                }
            }
        }

        long answer = 0;
        for (int i = 0; i < 3; i++) {
            answer += dp[i][N - 1][N - 1];
        }
        System.out.println(answer);

    }

}
