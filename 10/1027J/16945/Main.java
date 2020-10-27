import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static int[] board;
    public static int Min;
    public static int cnt;

    public static void perm(int k, int used, int[] choice) {
        if (k == 9) {
            int[] results = { choice[0] + choice[1] + choice[2], choice[3] + choice[4] + choice[5],
                    choice[6] + choice[7] + choice[8], choice[0] + choice[3] + choice[6],
                    choice[1] + choice[4] + choice[7], choice[2] + choice[5] + choice[8],
                    choice[0] + choice[4] + choice[8], choice[6] + choice[4] + choice[2] };
            for (int i = 1; i < results.length; i++) {
                if (results[i] != results[i - 1]) {
                    return;
                }
            }
            int temp = 0;
            for (int i = 0; i < 9; i++) {
                temp += Math.abs(choice[i] - board[i]);
            }
            cnt += 1;
            Min = Math.min(Min, temp);
            return;
        }
        for (int i = 1; i <= 9; i++) {
            if ((used & (1 << i)) != 0)
                continue;
            choice[k] = i;
            perm(k + 1, used | (1 << i), choice);
            choice[k] = 0;
        }
    }

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new int[9];
        int count = 0;
        for (int y = 0; y < 3; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < 3; x++) {
                board[count] = Integer.parseInt(st.nextToken());
                count += 1;
            }
        }
        int[] choice = new int[9];
        Min = 100000000;
        perm(0, 0, choice);
        System.out.println(cnt);
        System.out.println(Min);
    }
}
